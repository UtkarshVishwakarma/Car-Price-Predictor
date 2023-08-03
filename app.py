import streamlit as st
import pandas as pd
import pickle

df = pickle.load(open('df.pkl', 'rb'))
model = pickle.load(open('model.pkl', 'rb'))

st.title("Car Price Predictor")

name = st.selectbox("Select The Car Model Below", sorted(df['name'].unique()))
company = st.selectbox("Select The Car Company Below", sorted(df['company'].unique()))
year = st.selectbox("Select The Car Year Below", sorted(df['year'].unique()))

col1, col2 = st.columns(2)

with col1:
    kms_driven = st.number_input("Enter The Car Kms Driven Below")

with col2:
    fuel_type = st.selectbox("Select The Car Fuel Type Below", df['fuel_type'].unique())

if st.button("Submit"):
    data = [[name, company, year, kms_driven, fuel_type]]
    prediction = model.predict(data)
    st.write(f'### The Range Price is: ₹ {round(prediction[0], 2)}')


