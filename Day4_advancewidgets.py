import streamlit as st

# Title of the app
st.title('Advanced Widgets in Streamlit')

##########  Select Box  ##########

st.subheader('Select Box')

# Adding a Selectbox
# Creates a dropdown menu that allows users to select one option from a list.
option = st.selectbox('Choose an option:', ['Option 1', 'Option 2', 'Option 3'])

# Display the selected option
st.write(f'You selected: {option}')

####################################

##########  Date Picker  ##########

st.subheader('Date picker')

# Adding Date Input
selected_date = st.date_input('Select a date')

# Display the selected date
# Creates a date picker for selecting dates.
st.write(f'You selected: {selected_date}')

####################################

##########  File Uploader  ##########

st.subheader('File uploader')

# Adding File Uploader
# Creates a file upload interface allowing users to upload files.
uploaded_file = st.file_uploader('Upload a file')

# Display the file name
if uploaded_file is not None:
    st.write(f'Uploaded file: {uploaded_file.name}')

####################################

##########  Radio Button  ##########

st.subheader('Radio Button')

# Adding Radio Buttons
# Creates radio buttons for selecting a single option from a list.
choice = st.radio('Pick a choice:', ['Choice 1', 'Choice 2', 'Choice 3'])

# Display the selected choice
st.write(f'You selected: {choice}')

####################################

