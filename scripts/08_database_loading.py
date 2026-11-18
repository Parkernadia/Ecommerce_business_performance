
import getpass
from pathlib import Path

import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.engine import URL

# ================================================================
# DATABASE CONFIGURATION
# ================================================================

PROJECT_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_DIR / "data" / "processed"

DATABASE = "ecommerce_business_performance 4."
USERNAME = "postgres"
HOST = "localhost"
PORT = 5432

password = getpass.getpass("Enter your PostgreSQL password: ")

connection_url = URL.create(
    drivername="postgresql+psycopg2",
    username=USERNAME,
    password=password,
    host=HOST,
    port=PORT,
    database=DATABASE
)

engine = create_engine(connection_url)

# ================================================================
# DATASET LOADING
# ================================================================

datasets = {
    "website_sessions": "website_sessions.csv",
    "website_pageviews": "website_pageviews.csv",
    "orders": "orders.csv",
    "order_items": "order_items.csv",
    "order_item_refunds": "order_item_refunds.csv",
    "products": "products.csv"
}

print("=" * 65)
print("DATABASE LOADING")
print("=" * 65)

try:
    with engine.connect() as connection:
        print(f"\nConnected to database: {DATABASE}")

    for table_name, file_name in datasets.items():
        file_path = DATA_DIR / file_name

        print(f"\nLoading: {table_name}")

        data = pd.read_csv(
            file_path,
            parse_dates=["created_at"]
        )

        data.to_sql(
            name=table_name,
            con=engine,
            if_exists="replace",
            index=False,
            chunksize=5000,
            method="multi"
        )

        print(f"Rows loaded: {len(data):,}")

    print("\n" + "=" * 65)
    print("DATABASE LOADING COMPLETED")
    print("=" * 65)

except Exception as error:
    print("\nDATABASE LOADING FAILED")
    print(error)

finally:
    engine.dispose()