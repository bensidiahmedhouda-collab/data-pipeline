import streamlit as st
from src.extract import fetch_daily_stock_data
from src.transform import transform_stock_data

st.title("AMZN Stock Dashboard")

@st.cache_data
def load_data():
    df = fetch_daily_stock_data("AMZN")
    return transform_stock_data(df)

df = load_data()

st.subheader("This Week's Performance")
week = df.tail(5)
cols = st.columns(len(week))
for col, (date, row) in zip(cols, week.iterrows()):
    col.metric(
        label=date.strftime("%a %b %d"),
        value=f"${row['close']:.2f}",
        delta=f"{row['daily_return']:.2f}%"
    )

st.subheader("Closing Price Over Time")
st.line_chart(df["close"])

st.subheader("7-Day Moving Average")
st.line_chart(df["moving_average_7"].dropna())

st.subheader("Last 10 Rows")
st.dataframe(df.tail(10))
