import streamlit as st

# Set page configuration
st.set_page_config(page_title="Crop Recommendation", page_icon="🌱", layout="wide")

background_image = """
<style>
[data-testid="stAppViewContainer"] > .main {
    background-image: url("https://images.unsplash.com/photo-1613036582025-ba1d4ccb3226?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NDB8fGxvYW15JTIwc29pbHxlbnwwfHwwfHx8MA%3D%3D");
    background-size: cover;  
    background-position: cover;  
    background-repeat: no-repeat;
}
[data-testid="stHeader"]{
    background-color: rgba(0,0,0,0);
}
[data-testid="stToolbar"]{
    right: 2rem;
}
</style>
"""
hide_menu = """
<style>
#MainMenu {
    visibility: hidden;
}
[data-testid="stDeployButton"] {
    visibility: hidden;
</style>
"""
st.markdown(background_image, unsafe_allow_html=True)
st.markdown(hide_menu, unsafe_allow_html=True)

# Contact Us page content
st.title("Contact Us")
st.write("Feel free to reach out to us if you have any questions, suggestions, or feedback!")
st.subheader("Email")
st.write("Email: info@smartsoil.com")
st.subheader("Phone")
st.write("Phone: +1234567890")
st.subheader("Address")
st.write("123 Main Street")
st.write("Karachi, Sindh, Pakistan")
