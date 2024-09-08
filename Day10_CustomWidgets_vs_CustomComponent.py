import streamlit as st
import pandas as pd
import streamlit.components.v1 as components

################### Custom Widgets #################
#Sample data
data = pd.DataFrame({
    'Name': ['John', 'Jane', 'Alice', 'Bob'],
    'Age': [23, 25, 31, 35],
    'Occupation': ['Engineer', 'Doctor', 'Artist', 'Designer']
})

st.title("Filter the Data")

# Create custom widgets for filtering
age_filter = st.slider("Select Age Range:", min_value=20, max_value=40, value=(20, 40))
occupation_filter = st.selectbox("Select Occupation:", data['Occupation'].unique())

# Apply filters to the data
filtered_data = data[(data['Age'].between(age_filter[0], age_filter[1])) & 
                     (data['Occupation'] == occupation_filter)]

# Display filtered data
st.write(f"Filtered Data based on age and occupation:", filtered_data)
######################################################

################### Custom Components ###################

# Define a custom component with HTML and JavaScript for a live-updating stock chart
def custom_stock_chart():
    html_code = """
    <div id="stock-chart"></div>
    <script>
    var chart = document.getElementById('stock-chart');
    function updateChart() {
        var price = Math.random() * 100;  // Simulate stock price data
        chart.innerHTML = '<h2 style="color: green;">Live Stock Price: $' + price.toFixed(2) + '</h2>';
    }
    setInterval(updateChart, 1000);  // Update every second
    </script>
    """
    return components.html(html_code)

st.title("Real-Time Stock Price Dashboard")
custom_stock_chart()

######################################################

