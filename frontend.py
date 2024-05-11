import streamlit as st

st.set_page_config(page_title="Crop Recommendation")
background_image = """
<style>
[data-testid="stAppViewContainer"] > .main {
    background-image: url("https://images.wallpaperscraft.com/image/single/texture_soil_sand_50620_1600x900.jpg");
    background-size: 100vw 100vh;  
    background-position: center;  
    background-repeat: no-repeat;
}

[data-testid = "stHeader"]{
    background-color : rgba(0,0,0,0);
}

[data-testid = "stToolbar"]{
    right: 2rem;
}
</style>
"""

st.markdown(background_image, unsafe_allow_html=True)



# Streamlit app content
st.title('Soil Recommendation App')
st.subheader('Welcome to the Soil Recommendation App')
st.write("Our Crop Recommendation App **FOR COTTON** is designed to assist you in making informed decisions tailored to these specific soil features. With just a few clicks, you can input the soil nutrient levels of zinc, boron, phosphorus, potassium, and sulfur, and our app will analyze the data to provide you with personalized crop recommendations optimized for your cotton soil conditions.")

st.header("Feature Selection")

# Define the available features in the dropdown menu
features = ['Boron', 'Zinc', 'Phosphorus', 'Potassium', 'Sulfur']
    
# Display dropdown menu to select features
selected_features = st.multiselect("Select features:", features)

# Default values for features
default_values = {
    'Boron': 1.3,
    'Zinc': 13,
    'Phosphorus': 63,
    'Potassium': 135,
    'Sulfur': 13.5
}
# Make a copy of default values before user input
user_values = default_values.copy()

# Prompt user to enter values for selected features

if selected_features :
    st.write("**Note: Features not Selected will be given a default value**")
    st.write("**Selected Features are given default values already, feel free to change by your own**")
    for feature in selected_features:
        user_input = st.number_input(f"Enter value for {feature}:", value=default_values[feature])
        user_values[feature] = user_input

# Display user input values after confirming
if st.button("Confirm"):

# Display selected features and default values side by side
    if selected_features:
        col1, col2 = st.columns(2)
        with col1:
            st.write("Selected features :")
            for feature in selected_features:
                st.write(f"{feature}: {user_values[feature]}")
            for feature,value in default_values.items():
                if feature not in selected_features:
                    st.write(f"{feature}: {value}")
        with col2:
            st.write("Default features :")
            for feature in features:
                st.write(f"{feature}: {default_values[feature]}")
                
            # Display the hard-coded recommendation
        if st.button('Predict The Soil'):
            st.write("Recommendations :")
            st.write("Based on the analysis, your soil seems suitable for cotton!")
                