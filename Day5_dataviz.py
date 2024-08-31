import streamlit as st
import pandas as pd
import numpy as np

# Title of the app
st.title('Data Visualization in Streamlit')

# Generating sample data
data = pd.DataFrame(np.random.randn(50, 3), columns=['A', 'B', 'C'])

# Step 1: Creating a Line Chart
st.subheader('Line Chart')
st.write("Line charts are excellent for visualizing trends over time.")
st.line_chart(data)

# Generating sample data
data = pd.DataFrame(np.random.randn(50, 3), columns=['A', 'B', 'C'])

# Step 2: Creating a Bar Chart
st.subheader('Bar Chart')
st.write("Bar charts are useful for comparing categorical data.")
st.bar_chart(data)


# Generating sample data
data = pd.DataFrame(np.random.randn(50, 3), columns=['A', 'B', 'C'])

# Step 3: Creating an Area Chart
st.subheader('Area Chart')
st.write("Area charts help show cumulative data trends.")
st.area_chart(data)

# Step 4: Adding a Map Visualization for Bangalore
st.subheader('Map Visualization')
st.write("Map visualizations are useful for plotting geographical data.")

# Sample data for Map centered around Bangalore
map_data = pd.DataFrame({
    'lat': np.random.randn(100) / 50 + 12.97,  # Generate random latitudes around Bangalore (approx. 12.97°N)
    'lon': np.random.randn(100) / 50 + 77.59   # Generate random longitudes around Bangalore (approx. 77.59°E)
})

# Adding a Map
st.map(map_data)