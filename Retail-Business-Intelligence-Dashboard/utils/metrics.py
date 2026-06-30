def calculate_metrics(sales, users, products, carts):
    return {
        "Revenue": sales["total_cart_price"].sum(),
        "Customers": len(users),
        "Products": len(products),
        "Orders": len(carts),
        "Average Order": sales["total_cart_price"].mean()
    }