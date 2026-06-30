import pandas as pd
import os
import random

RAW_PATH = "data/raw/customers.csv"
PROCESSED_PATH = "data/processed/customers.csv"


def clean_customers():

    customers = pd.read_csv(RAW_PATH)

    # Remove duplicates
    customers.drop_duplicates(inplace=True)

    # Remove missing values
    customers.dropna(inplace=True)

    # Full Name
    customers["full_name"] = (
        customers["first_name"] + " " +
        customers["last_name"]
    )

    # Customer Segment
    customers["customer_segment"] = [
        random.choice(
            [
                "Regular",
                "Premium",
                "VIP"
            ]
        )
        for _ in range(len(customers))
    ]

    # Loyalty Score
    customers["loyalty_score"] = [
        random.randint(50,100)
        for _ in range(len(customers))
    ]

    # Region
    customers["region"] = customers["state"]

    os.makedirs(
        "data/processed",
        exist_ok=True
    )

    customers.to_csv(
        PROCESSED_PATH,
        index=False
    )

    print("✅ Customers cleaned successfully!")
    print(f"📁 Saved to: {PROCESSED_PATH}")


if __name__ == "__main__":
    clean_customers()