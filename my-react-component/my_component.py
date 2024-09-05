import streamlit.components.v1 as components

# Declare the component
_my_component = components.declare_component(
    "my_component",
    path="./frontend/build"
)

# Function to use the component
def my_component(message="Hello, Streamlit!"):
    return _my_component(message=message)

# Testing the component in Streamlit
import streamlit as st

st.title("Interactive React Component in Streamlit")

# Use the component
result = my_component(message="Hello from React !")
st.write("You typed:", result)
