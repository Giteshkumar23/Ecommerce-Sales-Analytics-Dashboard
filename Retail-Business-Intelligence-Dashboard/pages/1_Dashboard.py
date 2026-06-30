import streamlit as st
import plotly.express as px
import pandas as pd

from utils.loader import *
from utils.session import check_login

check_login()

# ===================================================
# PAGE CONFIG
# ===================================================

st.set_page_config(
    page_title="Smart Kirana Analytics",
    page_icon="🏪",
    layout="wide"
)

# ===================================================
# LOAD DATA
# ===================================================

sales = load_sales()
products = load_products()
customers = load_customers()
inventory = load_inventory()
categories = load_categories()
suppliers = load_suppliers()

# ===================================================
# SIDEBAR
# ===================================================

with st.sidebar:

    st.image(
        "https://img.icons8.com/color/96/shop.png",
        width=70
    )

    st.title("🏪 Smart Kirana")

    st.caption("Retail Business Intelligence")

    st.divider()

    st.success(f"👋 Welcome, {st.session_state.username}")

    st.write("### Navigation")

    st.info(
        "Use the menu above to explore analytics."
    )

    st.divider()

    st.write("### Current Status")

    st.success("🟢 System Online")

    st.divider()

    if st.button(
        "🚪 Logout",
        use_container_width=True
    ):

        st.session_state.logged_in = False
        st.session_state.username = ""

        st.switch_page("app.py")

    st.divider()

    st.info(
        "Monitor sales, inventory and customer activity."
    )

# ===================================================
# HEADER
# ===================================================

st.title("🏪 Smart Kirana Analytics")

st.caption("Indian Retail Business Intelligence Platform")

st.divider()

# ===================================================
# KPI VALUES
# ===================================================

total_sales = sales["total_amount"].sum()

total_profit = sales["profit"].sum()

total_customers = customers["customer_id"].nunique()

total_products = products["product_id"].nunique()

total_bills = sales["bill_no"].nunique()

inventory_value = inventory["inventory_value"].sum()

# ===================================================
# KPI SECTION
# ===================================================

st.subheader("📊 Business Overview")

c1, c2, c3 = st.columns(3)

with c1:
    st.metric(
        "💰 Total Sales",
        f"₹ {total_sales:,.0f}"
    )

with c2:
    st.metric(
        "👥 Customers",
        total_customers
    )

with c3:
    st.metric(
        "📦 Products",
        total_products
    )

c4, c5, c6 = st.columns(3)

with c4:
    st.metric(
        "🧾 Bills",
        total_bills
    )

with c5:
    st.metric(
        "💵 Profit",
        f"₹ {total_profit:,.0f}"
    )

with c6:
    st.metric(
        "📦 Inventory Value",
        f"₹ {inventory_value:,.0f}"
    )

st.divider()

# ===================================================
# SALES ANALYTICS
# ===================================================

st.subheader("📈 Sales Analytics")

left, right = st.columns(2)

# -----------------------------
# Monthly Sales
# -----------------------------

with left:

    monthly_sales = (
        sales.groupby("month")["total_amount"]
        .sum()
        .reset_index()
    )

    month_order = [
        "January","February","March","April",
        "May","June","July","August",
        "September","October","November","December"
    ]

    monthly_sales["month"] = pd.Categorical(
        monthly_sales["month"],
        categories=month_order,
        ordered=True
    )

    monthly_sales = monthly_sales.sort_values("month")

    fig = px.line(
        monthly_sales,
        x="month",
        y="total_amount",
        markers=True,
        title="Monthly Sales Trend"
    )

    fig.update_layout(
        template="plotly_dark",
        height=420,
        xaxis_title="",
        yaxis_title="Sales (₹)"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# -----------------------------
# Payment Mode
# -----------------------------

with right:

    payment = (
        sales.groupby("payment_mode")
        .size()
        .reset_index(name="count")
    )

    fig = px.pie(
        payment,
        names="payment_mode",
        values="count",
        hole=0.45,
        title="Payment Mode Distribution"
    )

    fig.update_layout(
        template="plotly_dark",
        height=420
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

st.divider()

# ===================================================
# INVENTORY & TOP PRODUCTS
# ===================================================

st.subheader("📦 Inventory & Product Performance")

left, right = st.columns(2)

# -----------------------------
# Inventory Status
# -----------------------------

with left:

    inventory_status = (
        inventory.groupby("stock_status")
        .size()
        .reset_index(name="count")
    )

    fig = px.bar(
        inventory_status,
        x="stock_status",
        y="count",
        color="stock_status",
        title="Inventory Status"
    )

    fig.update_layout(
        template="plotly_dark",
        height=420,
        xaxis_title="Stock Status",
        yaxis_title="Products"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# -----------------------------
# Top Selling Products
# -----------------------------

with right:

    top_products = (
        sales.groupby("product_id")["quantity"]
        .sum()
        .reset_index()
        .sort_values("quantity", ascending=False)
        .head(10)
    )

    top_products = top_products.merge(
        products,
        on="product_id"
    )

    fig = px.bar(
        top_products,
        x="quantity",
        y="product_name",
        orientation="h",
        color="quantity",
        title="Top 10 Selling Products"
    )

    fig.update_layout(
        template="plotly_dark",
        height=420,
        yaxis=dict(categoryorder="total ascending")
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

st.divider()

# ===================================================
# EXECUTIVE BUSINESS INSIGHTS
# ===================================================

st.subheader("🤖 Executive Business Insights")

c1, c2 = st.columns([2, 1])

with c1:

    best_product = (
        sales.groupby("product_id")["quantity"]
        .sum()
        .idxmax()
    )

    product_name = products.loc[
        products["product_id"] == best_product,
        "product_name"
    ].values[0]

    highest_profit = sales["profit"].sum()

    st.info(f"""
### 📈 Business Summary

🏆 Best Selling Product : **{product_name}**

💰 Total Profit : **₹ {highest_profit:,.0f}**

📦 Total Inventory Value : **₹ {inventory['inventory_value'].sum():,.0f}**

👥 Registered Customers : **{customers['customer_id'].nunique()}**

🧾 Bills Generated : **{sales['bill_no'].nunique()}**

💡 Recommendation:

Increase stock of **{product_name}** because it is currently your highest-selling product.
""")

with c2:

    low_stock = inventory[
        inventory["current_stock"] <= inventory["minimum_stock"]
    ]

    st.warning("### ⚠️ Low Stock Alerts")

    if len(low_stock) == 0:

        st.success("No products require restocking.")

    else:

        st.metric(
            "Products to Reorder",
            len(low_stock)
        )

        st.dataframe(
            low_stock[
                [
                    "product_id",
                    "current_stock",
                    "minimum_stock"
                ]
            ],
            use_container_width=True,
            hide_index=True
        )

st.divider()

# ===================================================
# RECENT SALES
# ===================================================

st.subheader("🧾 Recent Sales")

recent_sales = (
    sales.sort_values(
        "date",
        ascending=False
    )
    .head(10)
)

st.dataframe(
    recent_sales[
        [
            "bill_no",
            "date",
            "customer_id",
            "product_id",
            "quantity",
            "total_amount",
            "payment_mode"
        ]
    ],
    use_container_width=True,
    hide_index=True
)

st.divider()

st.markdown(
"""
<div style='text-align:center;color:gray;padding:20px'>

© 2026 Smart Kirana Analytics

Built with ❤️ using Python • Pandas • Plotly • Streamlit

Developed by <b>Gitesh Patel</b>

</div>
""",
unsafe_allow_html=True
)