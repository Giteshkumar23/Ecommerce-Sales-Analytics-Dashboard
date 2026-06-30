import pandas as pd
import random
import os
from datetime import datetime, timedelta

RAW_PATH = "data/raw"

products = pd.read_csv(
    os.path.join(RAW_PATH, "products.csv")
)

suppliers = pd.read_csv(
    os.path.join(RAW_PATH, "suppliers.csv")
)

inventory = []

warehouses = [
    "Raipur Warehouse",
    "Bhilai Warehouse",
    "Nagpur Warehouse"
]

today = datetime.today()

for _, product in products.iterrows():

    current_stock = random.randint(10, 250)

    minimum_stock = random.randint(20, 50)

    supplier = suppliers.sample(1).iloc[0]

    expiry = today + timedelta(
        days=random.randint(90, 720)
    )

    inventory.append({

        "product_id": product["product_id"],

        "supplier_id": supplier["supplier_id"],

        "warehouse": random.choice(warehouses),

        "current_stock": current_stock,

        "minimum_stock": minimum_stock,

        "inventory_value":
            current_stock * product["purchase_price"],

        "expiry_date":
            expiry.strftime("%Y-%m-%d")

    })

inventory = pd.DataFrame(inventory)

inventory.to_csv(
    os.path.join(RAW_PATH, "inventory.csv"),
    index=False
)

print("✅ Inventory Generated:", len(inventory))