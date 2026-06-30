import pandas as pd
import os

# -----------------------------
# Create folders
# -----------------------------

RAW_PATH = "data/raw"

os.makedirs(RAW_PATH, exist_ok=True)

# -----------------------------
# Categories
# -----------------------------

categories = pd.DataFrame({
    "category_id": range(1, 13),
    "category_name": [
        "Grocery",
        "Dairy",
        "Snacks",
        "Beverages",
        "Personal Care",
        "Household",
        "Baby Care",
        "Stationery",
        "Frozen Foods",
        "Health Care",
        "Spices",
        "Cleaning Supplies"
    ]
})

categories.to_csv(
    os.path.join(RAW_PATH, "categories.csv"),
    index=False
)

print("✅ Categories generated successfully!")