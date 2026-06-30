import pandas as pd
import random
import os
from datetime import datetime, timedelta

RAW_PATH = "data/raw"

products = pd.read_csv(os.path.join(RAW_PATH, "products.csv"))
customers = pd.read_csv(os.path.join(RAW_PATH, "customers.csv"))

payment_modes = [
    "UPI",
    "Cash",
    "Card"
]

sales = []

start_date = datetime(2025, 1, 1)

for bill in range(1, 10001):

    product = products.sample(1).iloc[0]

    customer = customers.sample(1).iloc[0]

    quantity = random.randint(1, 5)

    selling_price = product["selling_price"]

    subtotal = selling_price * quantity

    discount = random.choice([0, 10, 20, 30, 50])

    gst = subtotal * (product["gst_percent"] / 100)

    final_amount = subtotal + gst - discount

    sale_date = start_date + timedelta(
        days=random.randint(0, 365)
    )

    sales.append({

        "bill_no": f"BILL{bill:06d}",

        "date": sale_date.strftime("%Y-%m-%d"),

        "customer_id": customer["customer_id"],

        "product_id": product["product_id"],

        "quantity": quantity,

        "selling_price": selling_price,

        "discount": discount,

        "gst": round(gst, 2),

        "total_amount": round(final_amount, 2),

        "payment_mode": random.choice(payment_modes)

    })

sales = pd.DataFrame(sales)

sales.to_csv(
    os.path.join(RAW_PATH, "sales.csv"),
    index=False
)

print("✅ Sales Generated:", len(sales))