import streamlit as st

# Main application entry point
st.title("Crop Recommendation System")
st.write("Welcome to the Crop Recommendation System. Use the menu to navigate to different pages.")

# Load the navigation sidebar
st.sidebar.title("Navigation")
st.sidebar.write("Select a page to navigate")

# Use streamlit's built-in multi-page support by leveraging files in the "pages/" directory
st.sidebar.write("Go to pages using the sidebar.")
