import pandas as pd
import os

RAW_PATH = "data/raw/sales.csv"
PRODUCTS_PATH = "data/raw/products.csv"
PROCESSED_PATH = "data/processed/sales.csv"


def clean_sales():

    sales = pd.read_csv(RAW_PATH)

    products = pd.read_csv(PRODUCTS_PATH)

    # ----------------------------
    # Merge Product Information
    # ----------------------------

    sales = sales.merge(

        products[
            [
                "product_id",
                "purchase_price",
                "selling_price"
            ]
        ],

        on="product_id",

        how="left"

    )

    # ----------------------------
    # Profit
    # ----------------------------

    sales["profit"] = (

        (sales["selling_price_x"] -
         sales["purchase_price"])

        *

        sales["quantity"]

    ).round(2)

    # Rename column

    sales.rename(

        columns={

            "selling_price_x": "selling_price"

        },

        inplace=True

    )

    # Remove duplicate column

    sales.drop(

        columns=["selling_price_y"],

        inplace=True

    )

    # ----------------------------
    # Date Features
    # ----------------------------

    sales["date"] = pd.to_datetime(
        sales["date"]
    )

    sales["year"] = sales["date"].dt.year

    sales["month"] = sales["date"].dt.month_name()

    sales["quarter"] = sales["date"].dt.quarter

    sales["day"] = sales["date"].dt.day_name()

    os.makedirs(
        "data/processed",
        exist_ok=True
    )

    sales.to_csv(

        PROCESSED_PATH,

        index=False

    )

    print("✅ Sales cleaned successfully!")

    print(f"📁 Saved to: {PROCESSED_PATH}")


if __name__ == "__main__":

    clean_sales()