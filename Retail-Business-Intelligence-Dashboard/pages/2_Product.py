import streamlit as st
import plotly.express as px
import pandas as pd

from utils.loader import *
from utils.session import check_login

check_login()

st.set_page_config(
    page_title="Products",
    page_icon="📦",
    layout="wide"
)

products = load_products()

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
        
st.title("📦 Product Management") 

st.title("📦 Product Management")

st.caption("Smart Kirana Analytics")

st.divider()

# ==========================================
# KPI Cards
# ==========================================

total_products = len(products)

avg_price = products["selling_price"].mean()

avg_profit = products["profit_margin"].mean()

avg_gst = products["gst_percent"].mean()

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric(
        "Products",
        total_products
    )

with c2:
    st.metric(
        "Avg Selling Price",
        f"₹ {avg_price:.2f}"
    )

with c3:
    st.metric(
        "Avg Profit Margin",
        f"{avg_profit:.1f}%"
    )

with c4:
    st.metric(
        "Average GST",
        f"{avg_gst:.1f}%"
    )

st.divider()

# ==========================================
# Search
# ==========================================

search = st.text_input(
    "🔍 Search Product"
)

if search:

    products = products[
        products["product_name"]
        .str.contains(
            search,
            case=False
        )
    ]

# ==========================================
# Brand Filter
# ==========================================

brand = st.selectbox(
    "Select Brand",
    ["All"] +
    sorted(products["brand"].unique())
)

if brand != "All":

    products = products[
        products["brand"] == brand
    ]

st.success(
    f"{len(products)} Products Found"
)

st.divider()

# ==========================================
# Product Table
# ==========================================

st.subheader("📋 Product Catalog")

st.dataframe(

    products[

        [

            "product_name",

            "brand",

            "purchase_price",

            "selling_price",

            "profit",

            "profit_margin",

            "gst_percent"

        ]

    ],

    use_container_width=True,

    hide_index=True

)

st.divider()

# ==========================================
# PRODUCT ANALYTICS
# ==========================================

st.subheader("📊 Product Analytics")

left, right = st.columns(2)

# ------------------------------------------
# Profit Margin
# ------------------------------------------

with left:

    fig = px.bar(

        products.sort_values(
            "profit_margin",
            ascending=False
        ).head(10),

        x="product_name",

        y="profit_margin",

        color="profit_margin",

        title="Top 10 Profit Margin Products"

    )

    fig.update_layout(

        template="plotly_dark",

        height=420,

        xaxis_title="",

        yaxis_title="Profit Margin (%)"

    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# ------------------------------------------
# Brand Distribution
# ------------------------------------------

with right:

    brand_df = (

        products.groupby("brand")
        .size()
        .reset_index(name="count")

    )

    fig = px.pie(

        brand_df,

        names="brand",

        values="count",

        hole=0.45,

        title="Brand Distribution"

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

# ==========================================
# CATEGORY ANALYSIS
# ==========================================

st.subheader("🏷 Category Analysis")

category_df = (

    products.groupby("category_id")
    .size()
    .reset_index(name="Products")

)

fig = px.bar(

    category_df,

    x="category_id",

    y="Products",

    color="Products",

    title="Products per Category"

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

# ==========================================
# DOWNLOAD
# ==========================================

csv = products.to_csv(index=False)

st.download_button(

    "⬇ Download Products CSV",

    csv,

    file_name="products.csv",

    mime="text/csv",

    use_container_width=True

)

st.markdown(
"""
<div style='text-align:center;
padding:20px;
color:gray;'>

© 2026 Smart Kirana Analytics

Product Intelligence Dashboard

</div>
""",
unsafe_allow_html=True
)