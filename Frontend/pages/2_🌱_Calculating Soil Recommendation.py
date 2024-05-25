import streamlit as st
import numpy as np
from tensorflow.keras.models import load_model
from sklearn.preprocessing import StandardScaler
import joblib as joblib

# Load the trained models
model = joblib.load('D:/Crop-Recommendation/Model/knn_model.joblib')

# Initialize the scaler (use the same scaler you used during training)
scaler = joblib.load('D:/Crop-Recommendation/Model/scaler.pkl')

# Set page config
st.set_page_config(page_title="Crop Recommendation", page_icon="🌱", layout="wide")

background_image = """
<style>
[data-testid="stAppViewContainer"] > .main {
    background-image: url("https://images.unsplash.com/photo-1492496913980-501348b61469?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8c29pbHxlbnwwfHwwfHx8MA%3D%3D");
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
st.header("Feature Selection")

# Define the available features in the dropdown menu
features = ['Boron', 'Zinc', 'Phosphorus', 'Potassium', 'Sulfur', 'Nitrogen', 'Temperature']

# Display dropdown menu to select features
selected_features = st.multiselect("Select features:", features)

# Default values for features
default_values = {
    'Boron': 1.3,
    'Zinc': 13,
    'Phosphorus': 63,
    'Potassium': 135,
    'Sulfur': 13.5,
    'Nitrogen': 43.2,
    'Temperature': 34
}
user_values = {}

if selected_features:
    st.write("**Note: Features not Selected will be given a default value**")
    st.write("**Selected Features are given default values already, feel free to change by your own**")
    for feature in selected_features:
        user_input = st.number_input(f"Enter value for {feature}:", value=default_values[feature])
        user_values[feature] = user_input

if st.button("Confirm"):
    if selected_features:
        col1, col2 = st.columns(2)
        with col1:
            st.write("Selected features:")
            for feature in selected_features:
                st.write(f"{feature}: {user_values[feature]}")
            for feature, value in default_values.items():
                if feature not in selected_features:
                    st.write(f"{feature}: {value}")
        with col2:
            st.write("Default features:")
            for feature in features:
                st.write(f"{feature}: {default_values[feature]}")
        
        input_data = np.array([user_values[feature] for feature in features]).reshape(1, -1)
        print(input_data)
        input_data_normalized = scaler.fit_transform(input_data)
        prediction = model.predict(input_data_normalized)
        print(prediction)
        recommendation = "Based on the analysis, your soil seems suitable for cotton!" if prediction[0] >= 0.5 else "Based on the analysis, your soil does not seem suitable for cotton."
        # input_data = np.array([user_values[feature] for feature in features]).reshape(1, -1)
        # input_data_normalized = scaler.transform(input_data)
        # prediction_prob = model.predict(input_data_normalized)[0]
        # print(prediction_prob)  # Print the probability for debugging purposes

        # # Apply threshold to convert probabilities to binary predictions
        # prediction = 1 if prediction_prob >= 0.5 else 0

        # recommendation = "Based on the analysis, your soil seems suitable for cotton!" if prediction == 1 else "Based on the analysis, your soil does not seem suitable for cotton."


        st.write("Recommendations:")
        st.write(recommendation)
