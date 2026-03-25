import streamlit as st
from src.extract import fetch_daily_stock_data
from src.transform import transform_stock_data

st.title("AAPL Stock Dashboard")

@st.cache_data
def load_data():
    df = fetch_daily_stock_data("AAPL")
    return transform_stock_data(df)

df = load_data()

st.subheader("Closing Price Over Time")
st.line_chart(df["close"])

st.subheader("7-Day Moving Average")
st.line_chart(df["moving_average_7"].dropna())

st.subheader("Last 10 Rows")
st.dataframe(df.tail(10))
