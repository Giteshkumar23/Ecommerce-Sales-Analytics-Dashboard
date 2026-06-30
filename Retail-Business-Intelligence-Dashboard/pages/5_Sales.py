import streamlit as st
import plotly.express as px

from utils.loader import *
from utils.session import check_login

check_login()

st.set_page_config(
    page_title="Sales Analytics",
    page_icon="📈",
    layout="wide"
)
# ==========================================
# Sidebar
# ==========================================

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
sales = load_sales()
products = load_products()

sales = sales.merge(
    products[
        [
            "product_id",
            "product_name",
            "brand"
        ]
    ],
    on="product_id",
    how="left"
)

st.title("📈 Sales Analytics")

st.caption("Smart Kirana Analytics")

st.divider()

# =====================================
# KPI
# =====================================

total_sales = sales["total_amount"].sum()

total_profit = sales["profit"].sum()

avg_bill = sales["total_amount"].mean()

bills = sales["bill_no"].nunique()

c1, c2, c3, c4 = st.columns(4)

c1.metric(
    "Total Sales",
    f"₹ {total_sales:,.0f}"
)

c2.metric(
    "Total Profit",
    f"₹ {total_profit:,.0f}"
)

c3.metric(
    "Average Bill",
    f"₹ {avg_bill:.2f}"
)

c4.metric(
    "Bills",
    bills
)

st.divider()

# =====================================
# Monthly Sales
# =====================================

left, right = st.columns(2)

month_order = [
    "January","February","March","April",
    "May","June","July","August",
    "September","October","November","December"
]

monthly = (
    sales.groupby("month")["total_amount"]
    .sum()
    .reset_index()
)

monthly["month"] = monthly["month"].astype("category")
monthly["month"] = monthly["month"].cat.set_categories(
    month_order,
    ordered=True
)

monthly = monthly.sort_values("month")

with left:

    fig = px.line(
        monthly,
        x="month",
        y="total_amount",
        markers=True,
        title="Monthly Sales Trend"
    )

    fig.update_layout(
        template="plotly_dark",
        height=420
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# =====================================
# Payment Mode
# =====================================

with right:

    payment = (
        sales.groupby("payment_mode")
        .size()
        .reset_index(name="Count")
    )

    fig = px.pie(
        payment,
        names="payment_mode",
        values="Count",
        hole=.45,
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

# =====================================
# Top Selling Products
# =====================================

top = (
    sales.groupby("product_name")["quantity"]
    .sum()
    .reset_index()
    .sort_values(
        "quantity",
        ascending=False
    )
    .head(10)
)

fig = px.bar(
    top,
    x="product_name",
    y="quantity",
    color="quantity",
    title="Top Selling Products"
)

fig.update_layout(
    template="plotly_dark",
    height=450
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.divider()

# =====================================
# Recent Sales
# =====================================

st.subheader("🧾 Recent Sales")

st.dataframe(
    sales[
        [
            "bill_no",
            "date",
            "product_name",
            "quantity",
            "total_amount",
            "profit",
            "payment_mode"
        ]
    ].sort_values(
        "date",
        ascending=False
    ),
    use_container_width=True,
    hide_index=True
)

csv = sales.to_csv(index=False)

st.download_button(
    "⬇ Download Sales CSV",
    csv,
    file_name="sales.csv",
    mime="text/csv",
    use_container_width=True
)