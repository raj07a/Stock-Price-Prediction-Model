import streamlit as st
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
import numpy as np

# Title of the Dashboard
st.title("Stock Price Prediction Dashboard")

# Sidebar for User Inputs
st.sidebar.header("User Input Parameters")
stock_symbol = st.sidebar.text_input("Stock Symbol", "IBM")
start_date = st.sidebar.date_input("Start Date", value=pd.to_datetime("2022-01-01"))
end_date = st.sidebar.date_input("End Date", value=pd.to_datetime("2022-12-31"))

# Fetch Stock Data
def fetch_stock_data(symbol, start, end):
    try:
        data = yf.download(symbol, start=start, end=end, progress=False)
        data.reset_index(inplace=True)
        return data
    except Exception as e:
        st.error(f"Error fetching data: {e}")
        return None

# Load and Display Data
if st.sidebar.button("Fetch Data"):
    data = fetch_stock_data(stock_symbol, start_date, end_date)
    if data is not None:
        st.subheader(f"Historical Data for {stock_symbol}")
        st.write(data.head())

        # Plot Closing Prices
        st.subheader("Closing Price Trend")
        plt.figure(figsize=(10, 6))
        plt.plot(data['Date'], data['Close'], label='Closing Price', color='blue')
        plt.title(f"Closing Price Trend for {stock_symbol}")
        plt.xlabel("Date")
        plt.ylabel("Closing Price")
        plt.legend()
        st.pyplot(plt)

        # Data Scaling for Prediction (Optional Placeholder)
        st.subheader("Data Scaling (For Model Input)")
        scaler = MinMaxScaler(feature_range=(0, 1))
        scaled_data = scaler.fit_transform(data['Close'].values.reshape(-1, 1))
        st.write("Scaled Data Sample:", scaled_data[:5])

# Future Integration: Add model prediction outputs here
st.sidebar.markdown("---")
st.sidebar.subheader("Future Work")
st.sidebar.write("- Add Model Prediction")
st.sidebar.write("- Display Forecasted Prices")
