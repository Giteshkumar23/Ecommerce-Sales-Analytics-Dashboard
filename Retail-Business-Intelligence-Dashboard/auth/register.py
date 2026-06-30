import streamlit as st
from auth.auth import register_user


def show_register():

    st.title("📝 Create Account")
    st.caption("Register to access Smart Kirana Analytics")
    st.divider()

    with st.form("register_form"):

        full_name = st.text_input("👤 Full Name")
        email = st.text_input("📧 Email")
        mobile = st.text_input("📱 Mobile Number")
        username = st.text_input("👤 Username")
        password = st.text_input("🔒 Password", type="password")
        confirm_password = st.text_input("🔒 Confirm Password", type="password")

        submitted = st.form_submit_button(
            "Create Account",
            use_container_width=True
        )

        if submitted:

            if not all([
                full_name.strip(),
                email.strip(),
                mobile.strip(),
                username.strip(),
                password.strip(),
                confirm_password.strip()
            ]):
                st.error("Please fill all fields.")

            elif password != confirm_password:
                st.error("Passwords do not match.")

            else:
                success, message = register_user(
                    full_name,
                    email,
                    mobile,
                    username,
                    password
                )

                if success:
                    st.success(message)
                else:
                    st.error(message)