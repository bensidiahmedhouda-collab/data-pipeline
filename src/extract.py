import os
import requests
import pandas as pd
from dotenv import load_dotenv

load_dotenv()


def fetch_daily_stock_data(symbol: str) -> pd.DataFrame:
    api_key = os.getenv("ALPHA_VANTAGE_API_KEY")
    url = "https://www.alphavantage.co/query"
    params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": symbol,
        "outputsize": "compact",
        "apikey": api_key,
    }

    response = requests.get(url, params=params)
    response.raise_for_status()
    data = response.json()

    if "Time Series (Daily)" not in data:
        raise ValueError(f"Unexpected response for symbol '{symbol}': {data}")

    time_series = data["Time Series (Daily)"]
    df = pd.DataFrame.from_dict(time_series, orient="index")
    df.index = pd.to_datetime(df.index)
    df.index.name = "date"
    df.columns = ["open", "high", "low", "close", "volume"]
    df = df.astype(float)
    df.sort_index(inplace=True)

    return df
