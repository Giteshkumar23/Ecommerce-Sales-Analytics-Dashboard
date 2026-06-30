import streamlit as st
import plotly.express as px

from utils.loader import *
from utils.session import check_login

check_login()

st.set_page_config(
    page_title="Inventory",
    page_icon="📦",
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

inventory = load_inventory()
products = load_products()

inventory = inventory.merge(
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

st.title("📦 Inventory Management")

st.caption("Smart Kirana Analytics")

st.divider()

# ==========================================
# KPI
# ==========================================

total_products = len(inventory)

low_stock = len(
    inventory[
        inventory["stock_status"] == "Low Stock"
    ]
)

inventory_value = inventory[
    "inventory_value"
].sum()

reorder = len(
    inventory[
        inventory["reorder_required"] == "Yes"
    ]
)

c1, c2, c3, c4 = st.columns(4)

c1.metric("Products", total_products)

c2.metric("Low Stock", low_stock)

c3.metric(
    "Inventory Value",
    f"₹ {inventory_value:,.0f}"
)

c4.metric(
    "Need Reorder",
    reorder
)

st.divider()

# ==========================================
# Charts
# ==========================================

left, right = st.columns(2)

with left:

    status_df = (
        inventory.groupby("stock_status")
        .size()
        .reset_index(name="Count")
    )

    fig = px.pie(
        status_df,
        names="stock_status",
        values="Count",
        hole=.45,
        title="Inventory Status"
    )

    fig.update_layout(
        template="plotly_dark",
        height=420
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

with right:

    top_stock = inventory.sort_values(
        "current_stock",
        ascending=False
    ).head(10)

    fig = px.bar(
        top_stock,
        x="product_name",
        y="current_stock",
        color="current_stock",
        title="Top Stock Available"
    )

    fig.update_layout(
        template="plotly_dark",
        height=420,
        xaxis_title=""
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

st.divider()

# ==========================================
# Expiry Analysis
# ==========================================

fig = px.histogram(
    inventory,
    x="days_to_expiry",
    nbins=20,
    title="Days Until Product Expiry"
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
# Inventory Table
# ==========================================

st.subheader("📋 Inventory Details")

st.dataframe(
    inventory,
    use_container_width=True,
    hide_index=True
)

csv = inventory.to_csv(index=False)

st.download_button(
    "⬇ Download Inventory CSV",
    csv,
    file_name="inventory.csv",
    mime="text/csv",
    use_container_width=True
)