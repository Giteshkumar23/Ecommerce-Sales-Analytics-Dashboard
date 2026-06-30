import streamlit as st
from auth.auth import login_user


def show_login():

    st.title("🏪 Smart Kirana Analytics")

    st.subheader("🔐 Login")

    st.caption("Login to continue")

    st.divider()

    username = st.text_input(
        "👤 Username"
    )

    password = st.text_input(
        "🔒 Password",
        type="password"
    )

    if st.button(
        "Login",
        use_container_width=True
    ):

        if login_user(username, password):

            st.session_state.logged_in = True
            st.session_state.username = username

            st.success("Login Successful!")

            st.rerun()

        else:

            st.error("Invalid Username or Password")

    st.divider()

    st.info(
        "Don't have an account? Register first."
    )