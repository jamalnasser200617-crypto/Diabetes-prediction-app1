import streamlit as st
import pickle
import numpy as np

# 1. Page Config
st.set_page_config(page_title="Diabetes Prediction", layout="centered")

# 2. Load the Model and Scaler safely
@st.cache_resource
def load_files():
    try:
        model = pickle.load(open('model.pkl', 'rb'))
        scaler = pickle.load(open('scaler.pkl', 'rb'))
        return model, scaler
    except:
        return None, None

model, scaler = load_files()

# 3. UI
st.title('Diabetes Prediction System 🩺')

if model is None or scaler is None:
    st.error("⚠️ Error: 'model.pkl' or 'scaler.pkl' files are missing in GitHub!")
else:
    st.write('Enter the following clinical data:')
    
    col1, col2 = st.columns(2)
    with col1:
        f1 = st.number_input('Pregnancies', min_value=0, step=1)
        f2 = st.number_input('Glucose', min_value=0)
        f3 = st.number_input('Blood Pressure', min_value=0)
        f4 = st.number_input('Skin Thickness', min_value=0)
    with col2:
        f5 = st.number_input('Insulin', min_value=0)
        f6 = st.number_input('BMI', min_value=0.0, format="%.1f")
        f7 = st.number_input('Diabetes Pedigree', min_value=0.0, format="%.3f")
        f8 = st.number_input('Age', min_value=0, step=1)

    st.markdown("---")
    if st.button('Predict Result'):
        # Correctly formatted input
        input_features = np.array([[f1, f2, f3, f4, f5, f6, f7, f8]])
        
        # Scaling and Prediction
        input_scaled = scaler.transform(input_features)
        prediction = model.predict(input_scaled)
        
        if prediction[0] == 1:
            st.error('⚠️ The result indicates: **Diabetic**')
        else:
            st.success('✅ The result indicates: **Non-Diabetic**')
