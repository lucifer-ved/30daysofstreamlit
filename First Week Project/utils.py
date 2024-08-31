import pandas as pd
import yfinance as yf
import io

def create_watchlist_template():
    template_data = pd.DataFrame({'Ticker': ['AAPL', 'GOOGL', 'MSFT']})
    buffer = io.StringIO()
    template_data.to_csv(buffer, index=False)
    buffer.seek(0)
    return buffer.getvalue()

def get_current_price(ticker):
    try:
        stock = yf.Ticker(ticker)
        return stock.history(period='1d')['Close'].iloc[-1]
    except Exception as e:
        return None

def get_historical_data(ticker):
    try:
        stock = yf.Ticker(ticker)
        return stock.history(period='1y')[['Close']]
    except Exception as e:
        return pd.DataFrame()
