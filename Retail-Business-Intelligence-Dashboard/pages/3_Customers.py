import streamlit as st
import plotly.express as px

from utils.loader import *
from utils.session import check_login

check_login()

st.set_page_config(
    page_title="Customers",
    page_icon="👥",
    layout="wide"
)

customers = load_customers()
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

st.title("👥 Customer Management")

st.caption("Smart Kirana Analytics")

st.divider()

# ==================================
# KPI
# ==================================

total = len(customers)

vip = len(
    customers[
        customers["customer_segment"] == "VIP"
    ]
)

premium = len(
    customers[
        customers["customer_segment"] == "Premium"
    ]
)

regular = len(
    customers[
        customers["customer_segment"] == "Regular"
    ]
)

c1, c2, c3, c4 = st.columns(4)

c1.metric("Customers", total)
c2.metric("VIP", vip)
c3.metric("Premium", premium)
c4.metric("Regular", regular)

st.divider()

# ==================================
# Charts
# ==================================

left, right = st.columns(2)

with left:

    fig = px.pie(
        customers,
        names="customer_segment",
        title="Customer Segments",
        hole=.45
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

    state_df = (
        customers.groupby("state")
        .size()
        .reset_index(name="Customers")
        .sort_values(
            "Customers",
            ascending=False
        )
    )

    fig = px.bar(
        state_df,
        x="state",
        y="Customers",
        color="Customers",
        title="Customers by State"
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

# ==================================
# Loyalty Score
# ==================================

fig = px.histogram(
    customers,
    x="loyalty_score",
    nbins=20,
    title="Customer Loyalty Score"
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

# ==================================
# Customer Table
# ==================================

st.subheader("📋 Customer List")

st.dataframe(
    customers,
    use_container_width=True,
    hide_index=True
)

csv = customers.to_csv(index=False)

st.download_button(
    "⬇ Download Customers CSV",
    csv,
    file_name="customers.csv",
    mime="text/csv",
    use_container_width=True
)