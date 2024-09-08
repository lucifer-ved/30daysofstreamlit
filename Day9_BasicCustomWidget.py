import streamlit as st
from streamlit_option_menu import option_menu
import streamlit.components.v1 as components

def custom_greeting_widget(label, placeholder="Type your message..."):
    return st.text_input(label, placeholder)

st.title("Custom Greeting Widget")
user_message = custom_greeting_widget("Enter your greeting:")
st.write(f"You wrote: {user_message}")

st.title("Navigation Menu Example")

# Define the navigation menu
selected = option_menu(
    menu_title=None,
    options=["Home", "Profile", "Settings"],
    icons=["house", "person", "gear"],
    menu_icon="cast",
    default_index=0
)

st.write(f"Selected page: {selected}")

def custom_price_display(price):
    html_code = f"""
    <div style='font-size:24px; color:green;'>Current Price: ${price}</div>
    """
    return components.html(html_code)

st.title("Real-Time Pricing Widget")
custom_price_display(199.99)


