import streamlit as st
from PIL import Image
import pandas as pd
from components.data_cleaning import DataCleaning
import joblib
import time
logo = Image.open("src/resolve_tech_solutions_logo.jpg")
# Layout for top section with logo

model =  joblib.load("src/model/isolation_forest.pkl")
col1, col2 = st.columns([1, 4])
with col1:
    st.image(logo, width=100)  # Adjust width as needed
with col2:
    st.title("Anomaly Detection for Metric Data")

# Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Anamoly Detection"])

# Page Routing
if page == "Home":
    st.write("Anomaly Detection for Metric Data!")
    st.write("Select an option from the sidebar.")
elif page == "Anamoly Detection":
    st.subheader("Anamoly Detection")
    test_data = pd.read_csv("src/data/unseen_test_metric_data.csv")
    st.title("Real time simulation of Anamoly detection")
    st.write("Click the button below to start real-time anomaly detection")

    if st.button("Start Detection"):
        for i in range(len(test_data)):
            row =  test_data.iloc[[i]]
            data_cleaning = DataCleaning()
            cleaned_row = data_cleaning.clean(row)

            prediction =  model.predict(cleaned_row)[0]

            formatted_time = pd.to_datetime(row['timestamp'].values[0]).strftime('%d-%m-%Y  %H:%M:%S')
            st.write(f"**Record #{i+1} at {formatted_time}**")

            if prediction == -1:
                st.error("🚨 Anomaly Detected!")
            else:
                st.success("✅ Normal")
            time.sleep(5)


