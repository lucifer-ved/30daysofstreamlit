import streamlit as st
import pandas as pd
from utils import create_watchlist_template, get_current_price, get_historical_data

st.title('Stock Portfolio Insights Dashboard')

# Initialize or load portfolio and transaction data
if 'portfolio_data' not in st.session_state:
    st.session_state['portfolio_data'] = pd.DataFrame(columns=['Ticker', 'Shares', 'Current Price', 'Total Value'])
if 'transaction_log' not in st.session_state:
    st.session_state['transaction_log'] = pd.DataFrame(columns=['Action', 'Ticker', 'Shares', 'Price', 'Total Value', 'Timestamp'])

# Sidebar for adding or updating stock information
st.sidebar.header('Add/Edit Stock')
ticker = st.sidebar.text_input('Ticker (e.g., AAPL)', '')
shares = st.sidebar.number_input('Number of Shares', min_value=0, step=1)

# Handle stock addition or update
if st.sidebar.button('Add/Update Stock'):
    if ticker:
        current_price = get_current_price(ticker)
        if current_price:
            total_value = shares * current_price
            new_row = pd.DataFrame({
                'Ticker': [ticker],
                'Shares': [shares],
                'Current Price': [current_price],
                'Total Value': [total_value]
            })
            # Update or add stock information in the portfolio
            if ticker in st.session_state['portfolio_data']['Ticker'].values:
                st.session_state['portfolio_data'] = st.session_state['portfolio_data'][st.session_state['portfolio_data']['Ticker'] != ticker]
            st.session_state['portfolio_data'] = pd.concat([st.session_state['portfolio_data'], new_row], ignore_index=True).drop_duplicates()

            # Log the transaction
            transaction_log_entry = pd.DataFrame({
                'Action': ['Add/Update'],
                'Ticker': [ticker],
                'Shares': [shares],
                'Price': [current_price],
                'Total Value': [total_value],
                'Timestamp': [pd.Timestamp.now()]
            })
            st.session_state['transaction_log'] = pd.concat([st.session_state['transaction_log'], transaction_log_entry], ignore_index=True)

            st.success('Stock added/updated successfully!')
    else:
        st.error('Please enter a ticker.')

st.sidebar.markdown("---")  # Divider

# Sidebar for viewing recent transactions
st.sidebar.header('View Recent Transactions')
view_log = st.sidebar.checkbox('Show Recent Transactions')

st.sidebar.markdown("---")  # Divider

# Sidebar for managing watchlist
st.sidebar.header('Watchlist Management')

# Provide a downloadable CSV template for watchlist
st.sidebar.download_button(
    label="Download Watchlist Template",
    data=create_watchlist_template(),
    file_name="watchlist_template.csv",
    mime="text/csv"
)

# File uploader for watchlist CSV
uploaded_file = st.sidebar.file_uploader("Upload a CSV file with tickers", type="csv")

if uploaded_file is not None:
    # Display only the uploaded watchlist data
    watchlist_df = pd.read_csv(uploaded_file)
    
    # Validate the file content
    if 'Ticker' not in watchlist_df.columns:
        st.error("CSV must contain a 'Ticker' column.")
    else:
        tickers = watchlist_df['Ticker'].tolist()
        
        # Collect watchlist data
        watchlist_data = []
        for ticker in tickers:
            current_price = get_current_price(ticker)
            if current_price:
                watchlist_data.append({'Ticker': ticker, 'Current Price': current_price})
        
        # Display the watchlist
        st.header('Watchlist')
        if watchlist_data:
            st.dataframe(pd.DataFrame(watchlist_data), use_container_width=True)
        else:
            st.write('No valid tickers found in the watchlist.')
else:
    # Main content area when no file is uploaded
    if view_log:
        # Display recent transactions only
        st.header('Recent Transactions')
        if not st.session_state['transaction_log'].empty:
            st.dataframe(st.session_state['transaction_log'], use_container_width=True)
        else:
            st.write('No transactions to display.')
    else:
        # Display portfolio and stock price visualization
        if not st.session_state['portfolio_data'].empty:
            # Show stock price trends
            st.subheader('Stock Price Visualization')
            
            # Gather historical data for all tickers in the portfolio
            all_data = pd.DataFrame()
            for ticker in st.session_state['portfolio_data']['Ticker']:
                historical_data = get_historical_data(ticker)
                if not historical_data.empty:
                    historical_data['Ticker'] = ticker
                    all_data = pd.concat([all_data, historical_data])

            # Plot stock price trends
            if not all_data.empty:
                all_data.reset_index(inplace=True)
                st.line_chart(
                    all_data.pivot(index='Date', columns='Ticker', values='Close'),
                    use_container_width=True
                )
            
            # Show the portfolio table
            st.subheader('Portfolio Table')
            st.dataframe(st.session_state['portfolio_data'], use_container_width=True)
        else:
            st.write('Your portfolio is empty.')
