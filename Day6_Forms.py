import streamlit as st

# # Title of the app
# st.title('Forms in Streamlit')

# # Creating a Form
# with st.form(key='user_form'):
#     name = st.text_input('Name')
#     age = st.number_input('Age', min_value=0, max_value=100)
#     submit_button = st.form_submit_button(label='Submit')

# # Displaying the form data
# if submit_button:
#     st.write(f'Name: {name}, Age: {age}')

################################################################

# Title of the app
st.title('Advanced Form Handling in Streamlit')

# Creating a Form with Validation
with st.form(key='validation_form'):
    # Input fields
    username = st.text_input('Username')
    email = st.text_input('Email')
    age = st.number_input('Age', min_value=0, max_value=120)
    agree_to_terms = st.checkbox('I agree to the terms and conditions')
    
    # Form submission button
    submit_button = st.form_submit_button(label='Submit')

# Handling form submission
if submit_button:
    # Basic validation
    if not username or not email:
        st.error("Please fill out all fields.")
    elif not agree_to_terms:
        st.error("You must agree to the terms and conditions.")
    else:
        # If validation passes, process the form data
        st.success("Form submitted successfully!")
        st.write(f"Username: {username}")
        st.write(f"Email: {email}")
        st.write(f"Age: {age}")

################################################################

# Creating a form with validation
# with st.form(key='validation_form2'):
#     email = st.text_input('Email')
#     age = st.number_input('Age', min_value=0, max_value=100)
#     submit_button = st.form_submit_button(label='Submit')

# # Validating the form data
# if submit_button:
#     if "@" not in email:
#         st.error("Please enter a valid email address.")
#     else:
#         st.success(f'Email: {email}, Age: {age}')
