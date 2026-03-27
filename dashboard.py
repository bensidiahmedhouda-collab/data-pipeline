import streamlit as st
from src.extract import fetch_daily_stock_data
from src.transform import transform_stock_data

st.title("AMZN Stock Dashboard")

@st.cache_data
def load_data():
    df = fetch_daily_stock_data("AMZN")
    return transform_stock_data(df)

df = load_data()

latest = df.iloc[-1]
st.subheader("Today's Performance")
st.metric(
    label="Closing Price",
    value=f"${latest['close']:.2f}",
    delta=f"{latest['daily_return']:.2f}%"
)

st.subheader("Closing Price Over Time")
st.line_chart(df["close"])

st.subheader("7-Day Moving Average")
st.line_chart(df["moving_average_7"].dropna())

st.subheader("Last 10 Rows")
st.dataframe(df.tail(10))
