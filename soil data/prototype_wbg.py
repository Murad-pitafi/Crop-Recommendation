import streamlit as st 



background_image = """
<style>
[data-testid="stAppViewContainer"] > .main {
    background-image: url("https://source.unsplash.com/1600x900/?agriculture,soil");
    background-size: 100vw 100vh;  # This sets the size to cover 100% of the viewport width and height
    background-position: center;  
    background-repeat: no-repeat;
}
</style>
"""

st.markdown(background_image, unsafe_allow_html=True)

def analyze_image(image_bytes):
  # it will analyse image with cv and will return features of soil 
  # (e.g., soil texture, drainage, pH)
  
  features = {
    'texture': 'Sandy Loam',
    'drainage': 'Well Drained',
    'ph': 6.5
  }
  
  acceptable_range = {  
      'texture': ['Sandy Loam', 'Loam'],
      'drainage': ['Well Drained'],
      'ph':(6.0,6.5, 7.5)  
  }
  
  
  is_cotton_suitable = all(
    feature_value in acceptable_range[feature] for feature, feature_value in features.items()
 )
  
  
  recommendations = ['Consider crops like corn or soybeans']  # Default recommendation
  if is_cotton_suitable:
    recommendations = ['Based on the analysis, your soil seems suitable for cotton!']
  
  return {
    'features': features,
    'recommendations': recommendations
  }


st.title('Soil Analysis Prototype')

uploaded_file = st.file_uploader("Choose a Soil Image", type=["jpg", "png"])

if uploaded_file is not None:
  image = st.image(uploaded_file, width=250)
  results = analyze_image(uploaded_file.read())
  
  st.write("Identified Features:")
  st.text_area("", results['features'])  

  st.write("Recommendations:")
  st.text_area("", results['recommendations'])  
