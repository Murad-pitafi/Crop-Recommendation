import streamlit as st

# Set page configuration
st.set_page_config(page_title="Crop Recommendation", page_icon="🌱", layout="wide")

background_image = """
<style>
[data-testid="stAppViewContainer"] > .main {
    background-image: url("https://images.unsplash.com/photo-1613467590059-6f7ca215c61b?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8ODJ8fGNvdHRvbnxlbnwwfHwwfHx8MA%3D%3D");
    background-size: cover;  
    background-position: center;  
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
}
</style>
"""

st.markdown(background_image, unsafe_allow_html=True)
st.markdown(hide_menu, unsafe_allow_html=True)

# Homepage content
st.title('Soil Recommendation App')
st.header('Welcome to SmartSoil: Optimizing Cotton Cultivation')
st.write("Welcome to SmartSoil, your go-to destination for precision soil recommendations tailored specifically for cotton cultivation. At SmartSoil, we understand the vital role that soil composition plays in the success of your cotton crops. With our cutting-edge technology and expertise in artificial intelligence, we're revolutionizing the way farmers approach soil management, ensuring maximum yield and sustainability.")
st.write("Cotton, often referred to as **white gold**, is not just a crop; it's a lifeline for many communities around the globe. From the soft textiles that clothe us to the economic prosperity it brings to farmers, cotton holds immense significance. However, its successful cultivation hinges on several factors, with soil quality being chief among them.")
st.write("Understanding the intricacies of soil composition can be daunting, but fear not! SmartSoil simplifies this process by providing accurate soil recommendations tailored to the specific needs of cotton cultivation. Whether you're a seasoned farmer or just beginning your journey in agriculture, our platform empowers you with the knowledge and tools needed to optimize your crop yields while promoting environmental sustainability.")
st.write("Ready to take your cotton cultivation to the next level? Let's get started with SmartSoil!")
