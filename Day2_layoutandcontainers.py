# import streamlit as st

# # Main content
# st.title('Hello, Streamlit!!')
# st.write('Welcome to your first Streamlit application')

# # Add title to the sidebar.
# st.sidebar.title('Sidebar')

# # Creates a slider in the sidebar where users can select a value 
# # between 0 and 100. The default value is set to 50.
# slider_value = st.sidebar.slider('Select a value', 0, 100, 50)

# # Display the selected slider value in the main content area
# st.write(f'The selected value is {slider_value}')

# # Adds a button to the sidebar. 
# # If the button is clicked, the text “Sidebar button clicked!” 
# # is displayed in the main content area.
# if st.sidebar.button('Click me'):
#     st.write('Sidebar button clicked!')


# import streamlit as st

# # Main content
# st.title('Hello, Streamlit!!')
# st.write('Welcome to your first Streamlit application')

# ########### Sidebar ###########

# # Sidebar content
# st.sidebar.title('Sidebar')

# # Sidebar slider
# slider_value = st.sidebar.slider('Select a value', 0, 100, 50)

# # Display the selected slider value in the main content area
# st.write(f'The selected value is {slider_value}')

# # Sidebar button
# if st.sidebar.button('Click me'):
#     st.write('Sidebar button clicked!')

# ########### Sidebar ###########

# ########### Columns ###########

# # Creating columns
# col1, col2 = st.columns(2)

# # Adding content to columns
# with col1:
#     st.header('Column 1')
#     st.write('Content for the first column.')

# with col2:
#     st.header('Column 2')
#     st.write('Content for the second column.')

# ########### Columns ###########


import streamlit as st

# Main content
st.title('Hello, Streamlit!!')
st.write('Welcome to your first Streamlit application')

########### Sidebar ###########

# Add title to the sidebar.
st.sidebar.title('Sidebar')

# Creates a slider in the sidebar where users can select a value 
# between 0 and 100. The default value is set to 50.
slider_value = st.sidebar.slider('Select a value', 0, 100, 50)

# Display the selected slider value in the main content area
st.write(f'The selected value is {slider_value}')

# Adds a button to the sidebar. 
# If the button is clicked, the text “Sidebar button clicked!” 
# is displayed in the main content area.
if st.sidebar.button('Click me'):
    st.write('Sidebar button clicked!')
    
########### Sidebar ###########

########### Columns ###########

# Creates two columns in the main content area of the app.
col1, col2 = st.columns(2)

# Adding content to columns
with col1:
    st.header('Column 1')
    st.write('Content for the first column.')

with col2:
    st.header('Column 2')
    st.write('Content for the second column.')

########### Columns ###########

########### Container ###########

with st.container():
    st.header('This is a container')
    st.write('You can group multiple elements here.')
    st.write('Containers can be used to create sections within your app.')
    # Additional elements in the container
    st.button('Container Button')
    st.slider('Container Slider', 0, 10, 5)

########### Container ###########