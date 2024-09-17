import streamlit as st
import pandas as pd

################ LOADING & CACHING ############################

# Function to load data from a CSV file
@st.cache_data
def load_data(file_path):
    # Read the CSV file into a DataFrame
    return pd.read_csv(file_path)

# Path to your CSV file
file_path = 'path/to/your/large_real_estate_data.csv'

# Load the data
data = load_data(file_path)

# Display the number of rows in the dataset
st.write(f"Loaded {len(data)} properties.")

# Show the first few rows of the dataset
st.write(data.head())

# Display a chart if the necessary columns are present
if 'Price' in data.columns and 'City' in data.columns:
    avg_price_by_city = data.groupby('City')['Price'].mean()
    st.bar_chart(avg_price_by_city)
else:
    st.write("The dataset does not contain the 'Price' or 'City' columns.")

################################################################

# Function to load data from a CSV file
@st.cache_data
def load_data(file_path):
    # Read the CSV file into a DataFrame
    return pd.read_csv(file_path)

# Path to your CSV file
file_path = './large_real_estate_data.csv'

# Load the data
df = load_data(file_path)

# Filter properties by price range
min_price, max_price = st.slider('Select price range', 100000, 1000000, (200000, 800000))
filtered_data = df[(df['Price'] >= min_price) & (df['Price'] <= max_price)]

# Display the number of properties in the selected range
st.write(f"Properties in selected range: {len(filtered_data)}")

# Show the filtered data in a table
st.dataframe(filtered_data)

################################################################