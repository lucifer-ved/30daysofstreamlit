import streamlit as st
import pandas as pd
import sqlite3
import requests
import os
from dotenv import load_dotenv

#################### Connecting to SQLite ####################

#Cache the database connection using st.cache_resource
@st.cache_resource
def connect_db():
    conn = sqlite3.connect('imdb_movies.db')
    return conn

# Cache the data query using st.cache_data
@st.cache_data
def load_data(query):
    conn = connect_db()
    data = pd.read_sql(query, conn)
    conn.close()
    return data

# Fetch movies data with a filter
st.title("IMDB Movie Database")

query = """
SELECT title, year, genre, rating
FROM movies
WHERE year >= 2000
ORDER BY rating DESC
LIMIT 100
"""
movies_data = load_data(query)

st.write(movies_data)

############################################################

#################### Handling Live Data ####################

# Alpha Vantage API key
API_KEY = os.getenv('ALPHA_VANTAGE_API_KEY')

@st.cache_data(ttl=60)
def fetch_stock_data(symbol):
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval=1min&apikey={API_KEY}"
    response = requests.get(url)
    data = response.json()

    time_series = data['Time Series (1min)']
    df = pd.DataFrame.from_dict(time_series, orient='index')
    df.columns = ['Open', 'High', 'Low', 'Close', 'Volume']
    df.index = pd.to_datetime(df.index)

    return df

# Streamlit app
st.title("Real-Time Stock Price Data")

# User input for stock symbol
symbol = st.text_input("Enter Stock Symbol", value="AAPL")

if symbol:
    stock_data = fetch_stock_data(symbol)

    st.write(f"Showing real-time data for {symbol}")
    st.line_chart(stock_data[['Close']])
    st.dataframe(stock_data.head())

############################################################

#################### Handling Large Data ####################

# Cache the database connection
@st.cache_resource
def connect_db():
    return sqlite3.connect('imdb_movies.db')

# Function to load large datasets in chunks
def load_large_data(query, chunk_size=20):
    conn = connect_db()
    data_chunks = []
    for chunk in pd.read_sql(query, conn, chunksize=chunk_size):
        data_chunks.append(chunk)
    conn.close()
    return data_chunks

# Center title and content
st.markdown(
    """
    <style>
    .centered-title {
        text-align: center;
        margin-bottom: 20px;
    }
    .centered-table {
        margin-left: auto;
        margin-right: auto;
        width: 100%;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<h1 class="centered-title">Movie Data Viewer</h1>', unsafe_allow_html=True)

# Load and display data
query = "SELECT * FROM movies"
data_chunks = load_large_data(query)

# Create columns to center the content
col1, col2, col3 = st.columns([1, 3, 1])

with col2:  # Center column
    if data_chunks:
        st.write(data_chunks[0].style.set_table_attributes('class="centered-table"'))
    else:
        st.write("No data available.")

############################################################



