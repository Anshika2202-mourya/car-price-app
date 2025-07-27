import streamlit as st
import numpy as np
import joblib

# Load model and feature names
model = joblib.load("car_price_model.pkl")
features = joblib.load("feature_names.pkl")

st.title("🚗 Car Price Prediction App")
st.markdown("Enter the car details below to predict the selling price.")

user_inputs = []

# Create input fields dynamically based on features
for feature in features:
    value = st.number_input(f"Enter {feature}", step=1.0)
    user_inputs.append(value)

if st.button("Predict Price"):
    prediction = model.predict([user_inputs])[0]
    st.success(f"💰 Estimated Selling Price: ₹{int(prediction):,}")
