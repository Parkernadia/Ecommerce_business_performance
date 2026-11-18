from pathlib import Path

import pandas as pd


PROJECT_DIR = Path(__file__).resolve().parent.parent
RAW_DATA_DIR = PROJECT_DIR / "data" / "raw"

DATASETS = [
    "website_sessions.csv",
    "website_pageviews.csv",
    "orders_mav.csv",
    "order_items.csv",
    "order_item_refunds.csv",
    "products.csv",
    "maven_fuzzy_factory_data_dictionary.csv"
]


def inspect_dataset(file_name):
    file_path = RAW_DATA_DIR / file_name

    print("\n" + "=" * 70)
    print(f"DATASET: {file_name}")
    print("=" * 70)

    data = pd.read_csv(file_path, low_memory=False)

    print(f"\nRows: {data.shape[0]:,}")
    print(f"Columns: {data.shape[1]:,}")

    print("\nColumn names:")
    print(data.columns.tolist())

    print("\nData types:")
    print(data.dtypes)

    print("\nMissing values:")
    print(data.isnull().sum())

    print(f"\nDuplicate rows: {data.duplicated().sum():,}")

    print("\nFirst five rows:")
    print(data.head().to_string(index=False))


def main():
    for file_name in DATASETS:
        inspect_dataset(file_name)


if __name__ == "__main__":
    main()
    