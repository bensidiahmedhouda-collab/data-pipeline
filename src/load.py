import os
from datetime import date
import pandas as pd


def save_to_csv(df: pd.DataFrame, symbol: str) -> None:
    os.makedirs("data", exist_ok=True)
    today = date.today().strftime("%Y-%m-%d")
    filename = f"{symbol}_{today}.csv"
    filepath = os.path.join("data", filename)
    df.to_csv(filepath)
    print(f"Data saved to {filepath}")
