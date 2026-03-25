
from src.extract import fetch_daily_stock_data
from src.transform import transform_stock_data
from src.load import save_to_csv


df = fetch_daily_stock_data("AAPL")

print("Shape:", df.shape)
print("\nColumn names:", df.columns.tolist())
print("\nFirst 10 rows:")
print(df.head(10))
print("\nLast 5 rows:")
print(df.tail(5))
print("\nBasic stats:")
print(df.describe())


df_transformed = transform_stock_data(df)
print(df_transformed.head(10))


save_to_csv(df_transformed, "AAPL")