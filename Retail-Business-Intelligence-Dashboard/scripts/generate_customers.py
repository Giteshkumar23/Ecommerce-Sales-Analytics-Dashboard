import pandas as pd
import random
import os

RAW_PATH = "data/raw"

first_names = [
    "Rahul","Amit","Vivek","Rohit","Arjun","Suresh","Rakesh","Karan","Aditya","Manish",
    "Neha","Priya","Pooja","Sneha","Anjali","Kavita","Nisha","Riya","Simran","Aarti"
]

last_names = [
    "Sharma","Patel","Verma","Gupta","Singh","Yadav","Mishra","Jain",
    "Agarwal","Soni","Sahu","Patil","Kumar","Chauhan","Pandey"
]

cities = [
    "Raipur","Bhilai","Durg","Bilaspur","Raigarh",
    "Nagpur","Indore","Bhopal","Mumbai","Pune",
    "Delhi","Jaipur","Ahmedabad","Surat","Lucknow",
    "Hyderabad","Bengaluru","Chennai","Kolkata","Ranchi"
]

states = {
    "Raipur":"Chhattisgarh",
    "Bhilai":"Chhattisgarh",
    "Durg":"Chhattisgarh",
    "Bilaspur":"Chhattisgarh",
    "Raigarh":"Chhattisgarh",
    "Nagpur":"Maharashtra",
    "Mumbai":"Maharashtra",
    "Pune":"Maharashtra",
    "Indore":"Madhya Pradesh",
    "Bhopal":"Madhya Pradesh",
    "Delhi":"Delhi",
    "Jaipur":"Rajasthan",
    "Ahmedabad":"Gujarat",
    "Surat":"Gujarat",
    "Lucknow":"Uttar Pradesh",
    "Hyderabad":"Telangana",
    "Bengaluru":"Karnataka",
    "Chennai":"Tamil Nadu",
    "Kolkata":"West Bengal",
    "Ranchi":"Jharkhand"
}

customers = []

for customer_id in range(1,1001):

    first = random.choice(first_names)
    last = random.choice(last_names)

    city = random.choice(cities)

    phone = "9" + "".join(random.choices("0123456789",k=9))

    email = f"{first.lower()}.{last.lower()}{customer_id}@gmail.com"

    customers.append({

        "customer_id":customer_id,
        "first_name":first,
        "last_name":last,
        "city":city,
        "state":states[city],
        "mobile":phone,
        "email":email

    })

customers = pd.DataFrame(customers)

customers.to_csv(
    os.path.join(RAW_PATH,"customers.csv"),
    index=False
)

print("✅ Customers Generated:",len(customers))