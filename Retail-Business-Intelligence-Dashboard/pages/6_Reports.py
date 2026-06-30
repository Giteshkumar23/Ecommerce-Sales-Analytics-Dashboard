import streamlit as st

from utils.loader import *
from utils.session import check_login

check_login()

st.set_page_config(
    page_title="Reports",
    page_icon="📄",
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
customers = load_customers()
inventory = load_inventory()

st.title("📄 Reports Center")

st.caption("Generate and Export Business Reports")

st.divider()

st.subheader("📥 Export Reports")

c1, c2 = st.columns(2)

with c1:

    st.download_button(
        "⬇ Download Sales Report",
        sales.to_csv(index=False),
        file_name="sales_report.csv",
        mime="text/csv",
        use_container_width=True
    )

    st.download_button(
        "⬇ Download Products Report",
        products.to_csv(index=False),
        file_name="products_report.csv",
        mime="text/csv",
        use_container_width=True
    )

with c2:

    st.download_button(
        "⬇ Download Customers Report",
        customers.to_csv(index=False),
        file_name="customers_report.csv",
        mime="text/csv",
        use_container_width=True
    )

    st.download_button(
        "⬇ Download Inventory Report",
        inventory.to_csv(index=False),
        file_name="inventory_report.csv",
        mime="text/csv",
        use_container_width=True
    )

st.divider()

st.success("✅ Reports are ready for download.")