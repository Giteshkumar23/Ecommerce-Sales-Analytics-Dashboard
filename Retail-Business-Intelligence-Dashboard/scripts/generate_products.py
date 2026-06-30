import pandas as pd
import random
import os

RAW_PATH = "data/raw"

# --------------------------------
# Indian Brands
# --------------------------------

brands = {
    "Grocery": [
        "Aashirvaad", "Fortune", "India Gate",
        "Tata", "Patanjali"
    ],

    "Dairy": [
        "Amul", "Mother Dairy", "Nandini"
    ],

    "Snacks": [
        "Parle", "Britannia",
        "Haldiram", "Nestlé"
    ],

    "Beverages": [
        "Coca-Cola", "Pepsi",
        "Tata Tea", "Bru"
    ],

    "Personal Care": [
        "Colgate", "Dove",
        "Lux", "Clinic Plus"
    ],

    "Household": [
        "Surf Excel",
        "Ariel",
        "Vim",
        "Harpic"
    ],

    "Baby Care": [
        "Johnson's",
        "Pampers",
        "Himalaya"
    ],

    "Stationery": [
        "Classmate",
        "Cello",
        "Apsara"
    ],

    "Frozen Foods": [
        "McCain",
        "ITC"
    ],

    "Health Care": [
        "Dabur",
        "Himalaya",
        "Patanjali"
    ],

    "Spices": [
        "Everest",
        "MDH",
        "Catch"
    ],

    "Cleaning Supplies": [
        "Lizol",
        "Domex",
        "Colin"
    ]
}

# --------------------------------
# Products
# --------------------------------

items = {
    "Grocery": [
        "Atta", "Rice", "Sugar",
        "Salt", "Oil"
    ],

    "Dairy": [
        "Milk", "Butter",
        "Cheese", "Paneer",
        "Curd"
    ],

    "Snacks": [
        "Biscuits",
        "Chips",
        "Noodles",
        "Namkeen",
        "Cookies"
    ],

    "Beverages": [
        "Tea",
        "Coffee",
        "Juice",
        "Soft Drink"
    ],

    "Personal Care": [
        "Soap",
        "Toothpaste",
        "Shampoo",
        "Face Wash"
    ],

    "Household": [
        "Detergent",
        "Dishwash",
        "Floor Cleaner",
        "Toilet Cleaner"
    ],

    "Baby Care": [
        "Baby Powder",
        "Baby Soap",
        "Baby Lotion",
        "Diapers"
    ],

    "Stationery": [
        "Notebook",
        "Pen",
        "Pencil",
        "Marker"
    ],

    "Frozen Foods": [
        "French Fries",
        "Veg Nuggets",
        "Frozen Peas"
    ],

    "Health Care": [
        "Honey",
        "Chyawanprash",
        "Hand Sanitizer"
    ],

    "Spices": [
        "Turmeric",
        "Red Chilli",
        "Garam Masala",
        "Coriander Powder"
    ],

    "Cleaning Supplies": [
        "Glass Cleaner",
        "Bathroom Cleaner",
        "Disinfectant"
    ]
}

products = []

product_id = 1

for category_id, category in enumerate(items.keys(), start=1):

    for _ in range(20):

        brand = random.choice(brands[category])

        item = random.choice(items[category])

        purchase = random.randint(20, 400)

        selling = purchase + random.randint(10, 150)

        gst = random.choice([0, 5, 12, 18])

        products.append({

            "product_id": product_id,

            "product_name": f"{brand} {item}",

            "brand": brand,

            "category_id": category_id,

            "purchase_price": purchase,

            "selling_price": selling,

            "gst_percent": gst

        })

        product_id += 1

products = pd.DataFrame(products)

products.to_csv(
    os.path.join(RAW_PATH, "products.csv"),
    index=False
)

print("✅ Products Generated:", len(products))