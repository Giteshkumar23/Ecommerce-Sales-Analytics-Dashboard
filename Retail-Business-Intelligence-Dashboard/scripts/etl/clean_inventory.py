import pandas as pd
import os
from datetime import datetime

RAW_PATH = "data/raw/inventory.csv"
PROCESSED_PATH = "data/processed/inventory.csv"


def clean_inventory():

    inventory = pd.read_csv(RAW_PATH)

    inventory.drop_duplicates(inplace=True)
    inventory.dropna(inplace=True)

    # ----------------------------
    # Stock Status
    # ----------------------------

    inventory["stock_status"] = inventory.apply(
        lambda row:
        "Low Stock"
        if row["current_stock"] <= row["minimum_stock"]
        else "In Stock",
        axis=1
    )

    # ----------------------------
    # Days Until Expiry
    # ----------------------------

    today = datetime.today()

    inventory["expiry_date"] = pd.to_datetime(
        inventory["expiry_date"]
    )

    inventory["days_to_expiry"] = (
        inventory["expiry_date"] - today
    ).dt.days

    # ----------------------------
    # Reorder Required
    # ----------------------------

    inventory["reorder_required"] = inventory[
        "stock_status"
    ].apply(
        lambda x: "Yes" if x == "Low Stock" else "No"
    )

    os.makedirs(
        "data/processed",
        exist_ok=True
    )

    inventory.to_csv(
        PROCESSED_PATH,
        index=False
    )

    print("✅ Inventory cleaned successfully!")
    print(f"📁 Saved to: {PROCESSED_PATH}")


if __name__ == "__main__":
    clean_inventory()