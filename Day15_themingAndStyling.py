import streamlit as st

# Applying custom CSS using Streamlit's ability to embed HTML
st.markdown("""
    <style>
        h1 {
            font-family: 'Arial';
            color: #3cf;
            text-align: center;
        }

        .custom-button {
            background-color: #FF6347;
            color: white;
            padding: 10px 20px;
            border-radius: 5px;
            font-size: 18px;
            transition: background-color 0.3s ease;
        }

        .custom-button:hover {
            background-color: #FF4500;
        }
    </style>
""", unsafe_allow_html=True)

st.title("Theming & Styling in Streamlit")
st.markdown('<button class="custom-button">Click Me!</button>', unsafe_allow_html=True)
