from pathlib import Path

import pandas as pd


PROJECT_DIR = Path(__file__).resolve().parent.parent
RAW_DATA_DIR = PROJECT_DIR / "data" / "raw"


def load_dataset(file_name):
    return pd.read_csv(RAW_DATA_DIR / file_name, low_memory=False)


def main():
    orders = load_dataset("orders_mav.csv")
    order_items = load_dataset("order_items.csv")
    refunds = load_dataset("order_item_refunds.csv")

    print("\n" + "=" * 65)
    print("ORDER ITEM COUNT VALIDATION")
    print("=" * 65)

    item_counts = order_items.groupby("order_id").size()
    order_check = orders.set_index("order_id").join(
        item_counts.rename("actual_items")
    )

    count_mismatches = (
        order_check["items_purchased"] != order_check["actual_items"]
    ).sum()

    print(f"Orders with mismatched item counts: {count_mismatches:,}")

    print("\n" + "=" * 65)
    print("ORDER REVENUE VALIDATION")
    print("=" * 65)

    item_totals = order_items.groupby("order_id")["price_usd"].sum()
    revenue_check = orders.set_index("order_id").join(
        item_totals.rename("item_revenue")
    )

    revenue_check["difference"] = (
        revenue_check["price_usd"] - revenue_check["item_revenue"]
    )

    revenue_mismatches = (
        revenue_check["difference"].abs() > 0.01
    ).sum()

    print(f"Orders with revenue differences: {revenue_mismatches:,}")
    print(
        "Total absolute revenue difference: "
        f"${revenue_check['difference'].abs().sum():,.2f}"
    )

    print("\n" + "=" * 65)
    print("REFUND AMOUNT VALIDATION")
    print("=" * 65)

    refund_check = refunds.merge(
        order_items[["order_item_id", "price_usd"]],
        on="order_item_id",
        how="left"
    )

    excessive_refunds = (
        refund_check["refund_amount_usd"] > refund_check["price_usd"] + 0.01
    ).sum()

    print(f"Refunds exceeding item prices: {excessive_refunds:,}")

    print("\n" + "=" * 65)
    print("TEMPORAL CONSISTENCY")
    print("=" * 65)

    order_dates = orders[["order_id", "created_at"]].copy()
    item_dates = order_items.merge(
        order_dates,
        on="order_id",
        how="left",
        suffixes=("_item", "_order")
    )

    item_dates["created_at_item"] = pd.to_datetime(
        item_dates["created_at_item"]
    )
    item_dates["created_at_order"] = pd.to_datetime(
        item_dates["created_at_order"]
    )

    items_before_orders = (
        item_dates["created_at_item"] < item_dates["created_at_order"]
    ).sum()

    print(f"Order items dated before their orders: {items_before_orders:,}")

    refund_dates = refunds.merge(
        order_items[["order_item_id", "created_at"]],
        on="order_item_id",
        how="left",
        suffixes=("_refund", "_item")
    )

    refund_dates["created_at_refund"] = pd.to_datetime(
        refund_dates["created_at_refund"]
    )
    refund_dates["created_at_item"] = pd.to_datetime(
        refund_dates["created_at_item"]
    )

    refunds_before_items = (
        refund_dates["created_at_refund"] < refund_dates["created_at_item"]
    ).sum()

    print(f"Refunds dated before their order items: {refunds_before_items:,}")


if __name__ == "__main__":
    main()
    