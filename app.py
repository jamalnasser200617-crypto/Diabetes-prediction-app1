import streamlit as st
import pickle
import numpy as np

# 1. Load the Model and Scaler
# Make sure model.pkl and scaler.pkl are in the same GitHub folder
try:
    model = pickle.load(open('model.pkl', 'rb'))
    scaler = pickle.load(open('scaler.pkl', 'rb'))
except FileNotFoundError:
    st.error("Error: 'model.pkl' or 'scaler.pkl' not found. Please upload them to GitHub.")

# 2. App Interface Configuration
st.set_page_config(page_title="Diabetes Prediction", layout="centered")
st.title('Diabetes Prediction System 🩺')
st.write('Enter the following clinical data to get the prediction:')

# 3. Organizing inputs into two columns for better UI
col1, col2 = st.columns(2)

with col1:
    f1 = st.number_input('Pregnancies', min_value=0, step=1)
    f2 = st.number_input('Glucose (mg/dL)', min_value=0)
    f3 = st.number_input('Blood Pressure (mm Hg)', min_value=0)
    f4 = st.number_input('Skin Thickness (mm)', min_value=0)

with col2:
    f5 = st.number_input('Insulin (mu U/ml)', min_value=0)
    f6 = st.number_input('BMI (Weight/Height^2)', min_value=0.0, format="%.1f")
    f7 = st.number_input('Diabetes Pedigree Function', min_value=0.0, format="%.3f")
    f8 = st.number_input('Age', min_value=0, step=1)

# 4. Prediction Logic
st.markdown("---")
if st.button('Predict Result'):
    # Convert inputs to a numpy array
    input_features = np.array([[f1, f2, f3, f4, f5, f6, f7, f8]])
    
    # Apply Scaling
    input_scaled = scaler.transform(input_features)
    
    # Run Prediction
    prediction = model.predict(input_scaled)
    
    # Display Results
    if prediction[0] == 1:
        st.error('⚠️ The result indicates: **Diabetic**')
    else:
        st.success('✅ The result indicates: **Non-Diabetic**')
    
