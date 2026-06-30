from streamlit_option_menu import option_menu
import streamlit as st


def show_sidebar():
    with st.sidebar:
        selected = option_menu(
            menu_title="Navigation",
            options=[
                "Dashboard",
                "Products",
                "Customers",
                "Analytics",
                "ETL"
            ],
            icons=[
                "house",
                "box",
                "people",
                "bar-chart",
                "gear"
            ],
            menu_icon="shop",
            default_index=0,
            styles={
                "container": {
                    "padding": "10px",
                    "background-color": "#111827",
                },
                "icon": {
                    "color": "#4F46E5",
                    "font-size": "20px",
                },
                "nav-link": {
                    "font-size": "16px",
                    "text-align": "left",
                    "margin": "5px",
                    "--hover-color": "#1F2937",
                    "border-radius": "10px",
                },
                "nav-link-selected": {
                    "background-color": "#4F46E5",
                    "border-radius": "10px",
                },
            },
        )

    return selected