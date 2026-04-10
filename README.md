Diabetes Prediction System
An end-to-end Machine Learning web application that predicts the likelihood of diabetes in patients based on specific health metrics. Built with Python and deployed via Streamlit.

Live Demo
Check out the live app here:
(https://diabetes-prediction-app1-cajefinuetxjbo8caapm7v.streamlit.app/)

Table of Contents
Project Overview

Dataset Features

Technologies Used

How It Works

Installation and Local Setup

Project Structure

Project Overview
This project provides a screening tool for diabetes. By entering 8 clinical parameters, the system utilizes a Support Vector Machine (SVM) classifier to predict the patient's status. The goal is to demonstrate how AI can assist in medical diagnosis.

Dataset Features
The model analyzes 8 essential health indicators:

Pregnancies: Number of times pregnant.

Glucose: Plasma glucose concentration.

Blood Pressure: Diastolic blood pressure (mm Hg).

Skin Thickness: Triceps skin fold thickness (mm).

Insulin: 2-Hour serum insulin (mu U/ml).

BMI: Body mass index.

Diabetes Pedigree Function: Scores likelihood of diabetes based on family history.

Age: Age in years.

Technologies Used
Streamlit: For the web interface.

Scikit-Learn: For machine learning modeling and data scaling.

Pandas and NumPy: For data processing.

Pickle: For model serialization.

How It Works
Standardization: User inputs are processed via StandardScaler to match the training data distribution.

Classification: The pre-trained SVM model evaluates the scaled data.

Result: The app displays a Diabetic or Non-Diabetic result based on the model output.

Installation and Local Setup
To run this project on your machine:

Clone the repo:
git clone https://github.com/jamalnasser200617-crypto/Diabetes-prediction-app1.git

Install requirements:
pip install -r requirements.txt

Launch the app:
streamlit run app.py

Project Structure
app.py: Main Streamlit application

model.pkl: Trained SVM model file

scaler.pkl: Trained Scaler file

requirements.txt: Library dependencies

README.md: Project documentation

Disclaimer
This tool is for educational purposes only. It is not a substitute for professional medical diagnosis or treatment.
