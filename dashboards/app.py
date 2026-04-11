import streamlit as st
import requests

st.title("🚗 Smart Traffic Intelligence System")

st.subheader("Enter Route Details")

source = st.text_input("Source Location")
destination = st.text_input("Destination Location")

if st.button("Get Smart Route"):

    # Dummy features (replace later)
    features = [100, 120, 90, 110, 80, 5, 2]

    response = requests.post(
        "http://127.0.0.1:8000/predict",
        json={"features": features}
    )

    result = response.json()

    st.write("### 🚦 Traffic Prediction:", result["traffic_prediction"])
    st.write("### ⚠️ Risk Level:", result["risk_level"])