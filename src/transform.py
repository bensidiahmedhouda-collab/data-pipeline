import pandas as pd


def transform_stock_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["daily_return"] = df["close"].pct_change() * 100
    df["moving_average_7"] = df["close"].rolling(window=7).mean()
    df["is_positive_day"] = df["close"] > df["open"]
    return df
