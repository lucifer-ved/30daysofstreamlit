import streamlit as st

#################### BASIC SESSION MANAGEMENT #######

# Initialize a counter in session state
if 'counter' not in st.session_state:
    st.session_state.counter = 0

# Button to increment the counter
if st.button('Increment'):
    st.session_state.counter += 1

st.write(f"Counter value: {st.session_state.counter}")

#####################################################

#################### FORM STATE #####################

# Initialize form input in session state
if 'name' not in st.session_state:
    st.session_state.name = ''

# Create a form
with st.form(key='my_form'):
    name_input = st.text_input('Your Name:', value=st.session_state.name)
    submit_button = st.form_submit_button('Submit')

# Update session state
if submit_button:
    st.session_state.name = name_input

st.write(f"Hello, {st.session_state.name}!")

#####################################################

#################### MULTIPLE STATE #################

# Initialize multiple session state variables
# The session state manages both the current step and progress, 
# allowing multiple values to persist and update simultaneously 
# based on user interactions.
if 'step' not in st.session_state:
    st.session_state.step = 1

if 'progress' not in st.session_state:
    st.session_state.progress = 0

# Simulate a multi-step process
if st.button('Next Step'):
    st.session_state.step += 1
    st.session_state.progress += 20

st.write(f"Current Step: {st.session_state.step}")
st.progress(st.session_state.progress)

#####################################################



