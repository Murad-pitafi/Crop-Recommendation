import streamlit as st

# Set page configuration
st.set_page_config(page_title="Crop Recommendation", page_icon="🌱", layout="wide")

background_image = """
<style>
[data-testid="stAppViewContainer"] > .main {
    background-image: url("https://images.unsplash.com/photo-1603330410703-f4efd972b76d?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NDh8fGNvdHRvbiUyMGZpZWxkfGVufDB8fDB8fHww");
    background-size: cover;  
    background-position: center bottom;  
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

# About Us page content
st.title("About Us")
st.write("SmartSoil is a team of passionate individuals dedicated to revolutionizing the agricultural industry through technology.")
st.write("Our mission is to empower farmers with cutting-edge solutions for soil management and crop cultivation, ensuring sustainable practices and maximum yield.")
st.write("With expertise in artificial intelligence, data analytics, and agronomy, we're committed to driving innovation and fostering growth in the farming community.")
st.write("At SmartSoil, we believe in harnessing the power of technology to create a brighter future for agriculture and the planet.")
