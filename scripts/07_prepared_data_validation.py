from pathlib import Path

import pandas as pd


PROJECT_DIR = Path(__file__).resolve().parent.parent
PROCESSED_DATA_DIR = PROJECT_DIR / "data" / "processed"


DATASETS = [
    "website_sessions.csv",
    "website_pageviews.csv",
    "orders.csv",
    "order_items.csv",
    "order_item_refunds.csv",
    "products.csv",
]


def main():
    print("\n" + "=" * 65)
    print("PREPARED DATA VALIDATION")
    print("=" * 65)

    for file_name in DATASETS:
        file_path = PROCESSED_DATA_DIR / file_name
        data = pd.read_csv(file_path, low_memory=False)

        dates_valid = (
            pd.api.types.is_datetime64_any_dtype(
                pd.to_datetime(data["created_at"], errors="raise")
            )
        )

        print(f"\nDataset: {file_name}")
        print(f"Rows: {len(data):,}")
        print(f"Columns: {len(data.columns)}")
        print(f"Date conversion valid: {dates_valid}")
        print(f"Duplicate rows: {data.duplicated().sum():,}")
        print(f"Missing values: {data.isnull().sum().sum():,}")

    print("\nPrepared data validation completed.")


if __name__ == "__main__":
    main()