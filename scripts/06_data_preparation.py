from pathlib import Path

import pandas as pd


PROJECT_DIR = Path(__file__).resolve().parent.parent
RAW_DATA_DIR = PROJECT_DIR / "data" / "raw"
PROCESSED_DATA_DIR = PROJECT_DIR / "data" / "processed"


DATASETS = {
    "website_sessions.csv": "website_sessions",
    "website_pageviews.csv": "website_pageviews",
    "orders_mav.csv": "orders",
    "order_items.csv": "order_items",
    "order_item_refunds.csv": "order_item_refunds",
    "products.csv": "products",
}


def prepare_dataset(file_name, table_name):
    data = pd.read_csv(
        RAW_DATA_DIR / file_name,
        low_memory=False
    )

    data["created_at"] = pd.to_datetime(
        data["created_at"],
        errors="raise"
    )

    output_path = PROCESSED_DATA_DIR / f"{table_name}.csv"
    data.to_csv(output_path, index=False)

    print(
        f"{table_name}: {len(data):,} rows exported "
        f"with {len(data.columns)} columns"
    )


def main():
    PROCESSED_DATA_DIR.mkdir(parents=True, exist_ok=True)

    print("\n" + "=" * 65)
    print("DATA PREPARATION")
    print("=" * 65)

    for file_name, table_name in DATASETS.items():
        prepare_dataset(file_name, table_name)

    print("\nData preparation completed.")


if __name__ == "__main__":
    main()
    