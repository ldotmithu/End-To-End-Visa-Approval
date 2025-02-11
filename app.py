import streamlit as st
import pandas as pd
import joblib
import numpy as np
from pathlib import Path
from mlproject.pipeline.prediction_pipeline import prediction_pipeline


preprocess = joblib.load(Path("atrifacts\data_transfomation\preprocess.pkl")) 
model = joblib.load(Path("atrifacts\model_train\model.pkl"))

st.title("Visa Approval Prediction")


continent = st.selectbox('Select Continent', ['Asia', 'Africa', 'North America', 'Europe', 'South America', 'Oceania'])
education = st.selectbox('Education of Employee', ["Master's", "Bachelor's", "Doctorate", "High School"])
has_job_experience = st.selectbox('Job Experience', ['Yes', 'No'])
region = st.selectbox('Region of Employment', ['Northeast', 'South', 'Midwest', 'West', 'Island'])
prevailing_wage = st.number_input('Prevailing Wage', min_value=0, max_value=200000, step=1000)
unit_of_wage = st.selectbox('Unit of Wage', ['Year', 'Month', 'Hour', 'Week'])
full_time_position = st.selectbox('Full-time Position', ['Yes', 'No'])


input_data = {
    'continent': continent,
    'education_of_employee': education,
    'has_job_experience': "Y" if has_job_experience == 'Yes' else "N",
    'region_of_employment': region,
    'prevailing_wage': prevailing_wage,
    'unit_of_wage': unit_of_wage,
    'full_time_position': "Y" if full_time_position == 'Yes' else "N"
}


input_df = pd.DataFrame([input_data])


preprocess_data = preprocess.transform(input_df)
pipleine =prediction_pipeline()
if st.button('Predict Visa Approval'):
    
    prediction = pipleine.prediction(preprocess_data)
    
    if prediction == 1:
        st.success("Denied")
    else:
        st.error("Certified")
