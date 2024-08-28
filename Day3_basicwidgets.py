import streamlit as st

# Title of the app
st.title("Simple Task Manager")

# Text Input Widget
# Creates a text input field where users can enter text.
task = st.text_input("Enter a task:")

# Button Widget
# Creates a button that triggers an action when clicked.
if st.button("Add Task"):
    st.write(f"Task added: {task}")

# Slider Widget
# Adds a slider for selecting numeric values within a specified range.
priority = st.slider("Select task priority:", 1, 5, 3)
st.write(f"Priority level: {priority}")

# Checkbox Widget
# Provides a checkbox to toggle between True and False states.
if st.checkbox("Mark as completed"):
    st.write("Task marked as completed!")
