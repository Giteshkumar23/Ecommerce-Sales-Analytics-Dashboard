import streamlit as st

from auth.login import show_login
from auth.register import show_register

st.set_page_config(
    page_title="Smart Kirana Analytics",
    page_icon="🏪",
    layout="centered"
)

# ==============================
# Session State
# ==============================

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "page" not in st.session_state:
    st.session_state.page = "login"

# ==============================
# If Logged In
# ==============================

if st.session_state.logged_in:

    st.success("✅ Login Successful!")

    st.title("🏪 Smart Kirana Analytics")

    st.write(
        f"Welcome **{st.session_state.username}** 👋"
    )

    st.info(
        "Use the left sidebar to access Dashboard, Products, Customers, Inventory, Sales and Reports."
    )

    if st.button("🚪 Logout"):

        st.session_state.logged_in = False
        st.session_state.page = "login"

        st.rerun()

# ==============================
# Login / Register
# ==============================

else:

    c1, c2 = st.columns(2)

    with c1:

        if st.button(
            "🔐 Login",
            use_container_width=True
        ):

            st.session_state.page = "login"

    with c2:

        if st.button(
            "📝 Register",
            use_container_width=True
        ):

            st.session_state.page = "register"

    st.divider()

    if st.session_state.page == "login":

        show_login()

    else:

        show_register()