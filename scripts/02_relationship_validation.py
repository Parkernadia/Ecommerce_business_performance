from pathlib import Path

import pandas as pd


PROJECT_DIR = Path(__file__).resolve().parent.parent
RAW_DATA_DIR = PROJECT_DIR / "data" / "raw"


def load_dataset(file_name):
    return pd.read_csv(RAW_DATA_DIR / file_name, low_memory=False)


def check_relationship(child, child_column, parent, parent_column):
    unmatched = ~child[child_column].isin(parent[parent_column])

    print(
        f"{child_column} -> {parent_column}: "
        f"{unmatched.sum():,} unmatched records"
    )


def main():
    sessions = load_dataset("website_sessions.csv")
    pageviews = load_dataset("website_pageviews.csv")
    orders = load_dataset("orders_mav.csv")
    order_items = load_dataset("order_items.csv")
    refunds = load_dataset("order_item_refunds.csv")
    products = load_dataset("products.csv")

    print("\n" + "=" * 65)
    print("PRIMARY KEY VALIDATION")
    print("=" * 65)

    primary_keys = {
        "website_sessions": (sessions, "website_session_id"),
        "website_pageviews": (pageviews, "website_pageview_id"),
        "orders": (orders, "order_id"),
        "order_items": (order_items, "order_item_id"),
        "order_item_refunds": (refunds, "order_item_refund_id"),
        "products": (products, "product_id"),
    }

    for table_name, (data, column) in primary_keys.items():
        duplicates = data[column].duplicated().sum()
        print(f"{table_name}.{column}: {duplicates:,} duplicate keys")

    print("\n" + "=" * 65)
    print("FOREIGN KEY VALIDATION")
    print("=" * 65)

    check_relationship(pageviews, "website_session_id", sessions, "website_session_id")
    check_relationship(orders, "website_session_id", sessions, "website_session_id")
    check_relationship(orders, "user_id", sessions, "user_id")
    check_relationship(orders, "primary_product_id", products, "product_id")
    check_relationship(order_items, "order_id", orders, "order_id")
    check_relationship(order_items, "product_id", products, "product_id")
    check_relationship(refunds, "order_item_id", order_items, "order_item_id")
    check_relationship(refunds, "order_id", orders, "order_id")

    print("\n" + "=" * 65)
    print("REFUND ORDER CONSISTENCY")
    print("=" * 65)

    refund_check = refunds.merge(
        order_items[["order_item_id", "order_id"]],
        on="order_item_id",
        how="left",
        suffixes=("_refund", "_item")
    )

    inconsistent = (
        refund_check["order_id_refund"]
        != refund_check["order_id_item"]
    ).sum()

    print(f"Refunds linked to a different order: {inconsistent:,}")


if __name__ == "__main__":
    main() 
