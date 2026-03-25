from src.extract import fetch_daily_stock_data
from src.transform import transform_stock_data
from src.load import save_to_csv

symbol = "AAPL"

df = fetch_daily_stock_data(symbol)
df = transform_stock_data(df)
save_to_csv(df, symbol)
