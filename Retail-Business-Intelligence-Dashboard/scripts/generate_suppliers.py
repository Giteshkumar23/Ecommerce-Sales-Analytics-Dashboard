import pandas as pd
import random
import os

RAW_PATH = "data/raw"

suppliers = [
    ("Amul Distributor", "Raipur"),
    ("Nestlé India", "Delhi"),
    ("Britannia Foods", "Mumbai"),
    ("ITC Foods", "Kolkata"),
    ("Parle Products", "Mumbai"),
    ("Hindustan Unilever", "Mumbai"),
    ("Dabur India", "Ghaziabad"),
    ("Patanjali Ayurved", "Haridwar"),
    ("Tata Consumer", "Mumbai"),
    ("Fortune Foods", "Ahmedabad"),
    ("PepsiCo India", "Gurugram"),
    ("Coca-Cola India", "Gurugram"),
    ("Johnson & Johnson", "Mumbai"),
    ("Colgate India", "Mumbai"),
    ("Everest Spices", "Mumbai"),
    ("MDH Spices", "Delhi"),
    ("Catch Foods", "Noida"),
    ("McCain India", "Ahmedabad"),
    ("Godrej Consumer", "Mumbai"),
    ("Marico Ltd.", "Mumbai")
]

supplier_data = []

for supplier_id, (name, city) in enumerate(suppliers, start=1):

    supplier_data.append({
        "supplier_id": supplier_id,
        "supplier_name": name,
        "city": city,
        "contact_person": f"Manager {supplier_id}",
        "mobile": "9" + "".join(random.choices("0123456789", k=9))
    })

df = pd.DataFrame(supplier_data)

df.to_csv(
    os.path.join(RAW_PATH, "suppliers.csv"),
    index=False
)

print("✅ Suppliers Generated:", len(df))