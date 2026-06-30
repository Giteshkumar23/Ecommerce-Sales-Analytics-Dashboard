import pandas as pd
import os

RAW_PATH = "data/raw/products.csv"
PROCESSED_PATH = "data/processed/products.csv"


def clean_products():

    products = pd.read_csv(RAW_PATH)

    # Remove duplicates
    products.drop_duplicates(inplace=True)

    # Remove missing values
    products.dropna(inplace=True)

    # Profit Per Product
    products["profit"] = (
        products["selling_price"] -
        products["purchase_price"]
    )

    # Profit Margin %
    products["profit_margin"] = (
        products["profit"] /
        products["selling_price"] * 100
    ).round(2)

    # GST Amount
    products["gst_amount"] = (
        products["selling_price"] *
        products["gst_percent"] / 100
    ).round(2)

    os.makedirs("data/processed", exist_ok=True)

    products.to_csv(
        PROCESSED_PATH,
        index=False
    )


if __name__ == "__main__":
    clean_products()