from clean_products import clean_products
from clean_customers import clean_customers
from clean_inventory import clean_inventory
from clean_sales import clean_sales

print("=" * 50)
print("🚀 Starting ETL Pipeline...")
print("=" * 50)

clean_products()
print("✅ Products Processed")

clean_customers()
print("✅ Customers Processed")

clean_inventory()
print("✅ Inventory Processed")

clean_sales()
print("✅ Sales Processed")

print("=" * 50)
print("🎉 ETL Completed Successfully")
print("=" * 50)