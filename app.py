import streamlit as st
from model import predict_delay

st.title("📦 Smart Parcel Delay Prediction")

st.write("Predict whether a delivery will be delayed.")

distance = st.number_input("Distance (in km)", min_value=1)
traffic = st.selectbox("Traffic Level", ["Low", "Medium", "High"])
weather = st.selectbox("Weather Condition", ["Clear", "Rainy", "Storm"])
delivery_type = st.selectbox("Delivery Type", ["Standard", "Express"])

if st.button("Predict"):
    result = predict_delay(distance, traffic, weather, delivery_type)
    st.success(f"Delivery Status: {result}")
