# import numpy as np
# import pandas as pd
# # Number of samples (records)
# num_samples = 600

# # Generate synthetic data for cotton yield prediction
# data = {
#     'Soil pH': np.random.uniform(5.5, 8.5, num_samples),
#     'Soil Moisture (%)': np.random.uniform(10, 30, num_samples),
#     'Soil Texture': np.random.choice(['sandy', 'loamy', 'clayey'], num_samples),
#     'Organic Matter (%)': np.random.uniform(2, 10, num_samples),
#     'Nitrogen (ppm)': np.random.uniform(10, 100, num_samples),
#     'Phosphorus (ppm)': np.random.uniform(5, 50, num_samples),
#     'Potassium (ppm)': np.random.uniform(50, 300, num_samples),
#     'Temperature (°C)': np.random.uniform(20, 35, num_samples),
#     'Rainfall (mm)': np.random.uniform(200, 1000, num_samples),
# }

# # Convert Soil Texture to one-hot encoding
# soil_texture_encoded = pd.get_dummies(data['Soil Texture'])
# data.update(soil_texture_encoded)
# data.pop('Soil Texture')

# # Generate target variable (cotton yield) based on features
# # Assume a linear relationship with some noise
# data['Cotton Yield (kg/ha)'] = (
#     3000  # base yield
#     + 100 * data['Soil pH']
#     + 75 * data['Soil Moisture (%)']
#     + 50 * data['Organic Matter (%)']
#     + 0.5 * data['Nitrogen (ppm)']
#     + 0.3 * data['Phosphorus (ppm)']
#     + 0.2 * data['Potassium (ppm)']
#     - 75 * (data['Temperature (°C)'] - 25)**2  # parabolic penalty for temperature deviation
#     + 0.5 * data['Rainfall (mm)']
#     + np.random.normal(0, 200, num_samples)  # random noise
# )

# # Create a DataFrame
# df = pd.DataFrame(data)

# # Save the DataFrame to a CSV file
# file_path = 'D:/Crop-Recommendation/cotton_yield_synthetic_600.csv'
# df.to_csv(file_path, index=False)
# print("fle saved")
# file_path  # Return file path for downloading
import pandas as pd

data = pd.read_csv('D:/Crop-Recommendation/cotton_yield_synthetic_600.csv')
print(data.head())