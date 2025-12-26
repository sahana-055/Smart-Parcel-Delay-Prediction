import streamlit as st
from model import predict_priority

st.title("📊 Smart Debt Recovery & Case Prioritization System")

st.write("This system helps identify high-risk debt cases for better recovery management.")

# User Inputs
amount = st.number_input("Outstanding Amount (₹)", min_value=1000)
delay = st.selectbox("Payment Delay Duration", ["<30 days", "30-60 days", "60+ days"])
customer_type = st.selectbox("Customer Type", ["Individual", "Business"])
payment_history = st.selectbox("Past Payment History", ["Good", "Average", "Poor"])

if st.button("Analyze Case"):
    result = predict_priority(amount, delay, customer_type, payment_history)
    st.success(f"🔍 Recovery Priority: {result}")
