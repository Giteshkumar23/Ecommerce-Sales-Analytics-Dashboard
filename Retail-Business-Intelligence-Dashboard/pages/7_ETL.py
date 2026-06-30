import streamlit as st
import subprocess
import time
from utils.session import check_login

check_login()

st.set_page_config(
    page_title="ETL Pipeline",
    page_icon="⚙️",
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

st.title("⚙️ ETL Pipeline")

st.markdown("""
Run the complete ETL Pipeline.

The pipeline will:

✅ Fetch data from FakeStore API

✅ Transform Data

✅ Load Data Warehouse

✅ Refresh Dashboard
""")

st.divider()

if st.button("▶ Run ETL Pipeline", use_container_width=True):

    progress = st.progress(0)

    status = st.empty()

    status.info("Running Ingestion...")

    subprocess.run(["python","dashboard/ingestion.py"])

    progress.progress(30)

    time.sleep(1)

    status.info("Running Transformation...")

    subprocess.run(["python","dashboard/transformation.py"])

    progress.progress(60)

    time.sleep(1)

    status.info("Loading Data Warehouse...")

    subprocess.run(["python","dashboard/modeling.py"])

    progress.progress(100)

    status.success("✅ ETL Pipeline Completed Successfully!")
    
    st.divider()

st.markdown(
    """
    <div style='text-align:center;color:gray;padding:20px'>
        © 2026 <b>Sales Intelligence Platform</b><br>
        Developed by <b>Gitesh Patel</b> 🚀<br>
        Python | PostgreSQL | Pandas | Plotly | Streamlit
    </div>
    """,
    unsafe_allow_html=True
)