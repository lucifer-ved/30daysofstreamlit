import sqlite3
import streamlit as st

# Connect to the SQLite database
def get_db_connection():
    conn = sqlite3.connect('users.db')
    conn.row_factory = sqlite3.Row
    return conn

# Authenticate user based on credentials
def authenticate_user(username, password):
    conn = get_db_connection()
    user = conn.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password)).fetchone()
    conn.close()
    return user

# Initialize session state variables
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.username = None

# Define the login function
def login(username, password):
    user = authenticate_user(username, password)
    if user:
        st.session_state.logged_in = True
        st.session_state.username = user['username']
        st.success(f"Welcome, {st.session_state.username}!")  

        st.session_state.logged_in = False
        st.session_state.username = None

        if st.button("Logout", key="logout_button"):
            logout()
        
    else:
        st.error("Invalid credentials. Please try again.")

# Logout function
def logout():
    st.session_state.logged_in = False
    st.session_state.username = None
    st.session_state.username_input = ""  
    st.session_state.password_input = ""
    st.experimental_rerun()  # Re-run the app to reflect the logout

# App layout
st.title("Streamlit : Basic Auth")

if st.session_state.logged_in:
    # Logout button with a unique key
    if st.button("Logout", key="logout_button"):
        logout()  # Clear session state and re-render the app
else:
    st.subheader("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    # Login button with a unique key
    if st.button("Login", key="login_button"):
        login(username, password)
