import streamlit as st
import streamlit.components.v1 as components
from st_aggrid import AgGrid
import pandas as pd

###### Basic Custom Component ######

# Define a custom component function
def custom_message(message):
    html = f"<div style='color: blue;'>{message}</div>"
    # Renders HTML content in your Streamlit app.
    return components.html(html)

# Use the custom component in your Streamlit app
st.title("Basic Custom Component Example")
custom_message("Hello, Streamlit!")

####################################


###### Integrating 3rd party custom component ######

st.title("Using AgGrid in Streamlit")

# Sample data
data = {
    'Name': ['John', 'Anna', 'Peter', 'Linda'],
    'Age': [28, 24, 35, 32],
    'City': ['New York', 'Paris', 'Berlin', 'London']
}

df = pd.DataFrame(data)

# Display data in AgGrid
AgGrid(df)

#####################################################
