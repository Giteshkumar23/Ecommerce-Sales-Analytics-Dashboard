import pandas as pd
import os

BASE_PATH = "data/processed"


def load_products():
    return pd.read_csv(
        os.path.join(BASE_PATH, "products.csv")
    )


def load_customers():
    return pd.read_csv(
        os.path.join(BASE_PATH, "customers.csv")
    )


def load_sales():
    return pd.read_csv(
        os.path.join(BASE_PATH, "sales.csv")
    )


def load_inventory():
    return pd.read_csv(
        os.path.join(BASE_PATH, "inventory.csv")
    )


def load_suppliers():
    return pd.read_csv(
        "data/raw/suppliers.csv"
    )


def load_categories():
    return pd.read_csv(
        "data/raw/categories.csv"
    )