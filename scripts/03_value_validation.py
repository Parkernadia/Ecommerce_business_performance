from pathlib import Path

import pandas as pd


PROJECT_DIR = Path(__file__).resolve().parent.parent
RAW_DATA_DIR = PROJECT_DIR / "data" / "raw"


def load_dataset(file_name):
    return pd.read_csv(RAW_DATA_DIR / file_name, low_memory=False)


def check_dates(data, table_name):
    dates = pd.to_datetime(data["created_at"], errors="coerce")

    print(f"\n{table_name}.created_at")
    print(f"Invalid dates: {dates.isna().sum():,}")
    print(f"Earliest date: {dates.min()}")
    print(f"Latest date: {dates.max()}")


def check_numeric_values(data, table_name, columns):
    print(f"\n{table_name}")

    for column in columns:
        print(
            f"{column}: "
            f"Minimum = {data[column].min()}, "
            f"Negative values = {(data[column] < 0).sum():,}"
        )


def main():
    sessions = load_dataset("website_sessions.csv")
    pageviews = load_dataset("website_pageviews.csv")
    orders = load_dataset("orders_mav.csv")
    order_items = load_dataset("order_items.csv")
    refunds = load_dataset("order_item_refunds.csv")
    products = load_dataset("products.csv")

    print("\n" + "=" * 65)
    print("DATE VALIDATION")
    print("=" * 65)

    datasets = {
        "website_sessions": sessions,
        "website_pageviews": pageviews,
        "orders": orders,
        "order_items": order_items,
        "order_item_refunds": refunds,
        "products": products,
    }

    for table_name, data in datasets.items():
        check_dates(data, table_name)

    print("\n" + "=" * 65)
    print("BINARY FLAG VALIDATION")
    print("=" * 65)

    flags = {
        "website_sessions.is_repeat_session": sessions["is_repeat_session"],
        "order_items.is_primary_item": order_items["is_primary_item"],
    }

    for column, values in flags.items():
        print(f"{column}: {sorted(values.dropna().unique().tolist())}")

    print("\n" + "=" * 65)
    print("CATEGORICAL VALUE VALIDATION")
    print("=" * 65)

    print("\nDevice types:")
    print(sessions["device_type"].value_counts(dropna=False))

    print("\nMarketing sources:")
    print(sessions["utm_source"].value_counts(dropna=False))

    print("\n" + "=" * 65)
    print("NUMERIC VALUE VALIDATION")
    print("=" * 65)

    check_numeric_values(
        orders,
        "orders",
        ["items_purchased", "price_usd", "cogs_usd"]
    )

    check_numeric_values(
        order_items,
        "order_items",
        ["price_usd", "cogs_usd"]
    )

    check_numeric_values(
        refunds,
        "order_item_refunds",
        ["refund_amount_usd"]
    )


if __name__ == "__main__":
    main()
    