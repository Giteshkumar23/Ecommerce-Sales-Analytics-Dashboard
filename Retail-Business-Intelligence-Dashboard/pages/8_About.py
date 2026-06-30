import streamlit as st
from utils.session import check_login

check_login()

st.set_page_config(
    page_title="About",
    page_icon="ℹ️",
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

st.title("ℹ️ About This Project")

st.markdown("""
# 📊 Sales Intelligence Platform

This project demonstrates a complete Business Intelligence workflow.

## 🚀 Features

- ETL Pipeline
- PostgreSQL Data Warehouse
- Interactive Dashboard
- Customer Analytics
- Product Analytics
- Sales Intelligence
- CSV Export
- KPI Monitoring

## 🛠 Tech Stack

- Python
- Pandas
- PostgreSQL
- Plotly
- Streamlit

## 👨‍💻 Developed By

**Gitesh Patel**

B.Tech Information Technology

Data Analytics & Python Enthusiast
""")