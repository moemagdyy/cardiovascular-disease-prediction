
import streamlit as st
import pickle
import numpy as np

# Load model and scaler
model = pickle.load(open('cardio_model.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))

st.title("Cardiovascular Disease Prediction")

st.write("Enter patient information below:")

age = st.number_input("Age")
gender = st.selectbox("Gender (1 = Female, 2 = Male)", [1,2])
height = st.number_input("Height (cm)")
weight = st.number_input("Weight (kg)")
ap_hi = st.number_input("Systolic Blood Pressure")
ap_lo = st.number_input("Diastolic Blood Pressure")
cholesterol = st.selectbox("Cholesterol Level", [1,2,3])
gluc = st.selectbox("Glucose Level", [1,2,3])
smoke = st.selectbox("Smoking", [0,1])
alco = st.selectbox("Alcohol Intake", [0,1])
active = st.selectbox("Physical Activity", [0,1])

# BMI feature
if height > 0:
    BMI = weight / ((height / 100) ** 2)
else:
    BMI = 0

input_data = np.array([[
    0,
    age,
    gender,
    height,
    weight,
    ap_hi,
    ap_lo,
    cholesterol,
    gluc,
    smoke,
    alco,
    active,
    BMI
]])

input_data_scaled = scaler.transform(input_data)

if st.button("Predict"):

    prediction = model.predict(input_data_scaled)

    if prediction[0] == 1:
        st.error("Patient is likely to have cardiovascular disease.")
    else:
        st.success("Patient is unlikely to have cardiovascular disease.")
