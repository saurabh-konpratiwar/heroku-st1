import streamlit as st
import pandas as pd
import pickle as pk
import numpy as np


pickle_in = open('model_pickle','rb')
svc = pk.load(pickle_in)
def prediction(Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age):
    prediction = svc.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])
    print(prediction)
    return prediction

st.title("Diabetes Symptoms ")
html_temp = """
<div style="background-color:orange; padding:10px">
<h2 style="color:red;text-align:center;">Streamlit Diabetes Predictor </h2>
</div>
"""
st.markdown(html_temp, unsafe_allow_html=True)
Pregnancies = st.number_input("Pregnancies")
Glucose = st.number_input("Glucose")
BloodPressure = st.number_input("BloodPressure")
SkinThickness = st.number_input("SkinThickness")
Insulin = st.number_input("Insulin")
BMI = st.number_input("BMI")
DiabetesPedigreeFunction = st.number_input("DiabetesPedigreeFunction")
Age = st.number_input("Age")
result = ""
if st.button("Predict"):
        result = prediction(int(Pregnancies),int(Glucose),int(BloodPressure),int(SkinThickness),int(Insulin),float(BMI),float(DiabetesPedigreeFunction),int(Age))
        print('result',result[0])
    if result[0] == 1:
            result2 = 'patient has diabities'
            st.success('its seem {} and recommended you to go to your doctor '.format(result2))
    else:
            result2 = 'patient does\'nt have diabities'
            st.error('The output is {}'.format(result2))
