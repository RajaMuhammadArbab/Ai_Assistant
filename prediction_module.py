from sklearn.linear_model import LinearRegression
import joblib
import numpy as np
import streamlit as st



def prediction_ui():
    st.header("🔮 Predictive Modeling")

    model_choice = st.radio("Choose Model", ["House Price", "Student Performance"])

    if model_choice == "House Price":
        area = st.number_input("Area (sqft)", min_value=100)
        rooms = st.slider("Rooms", 1, 10)
        loc_score = st.slider("Location Score", 1, 10)
        if st.button("Predict Price"):
            model = joblib.load("models//house_model.pkl")
            prediction = model.predict([[area, rooms, loc_score]])
            st.success(f"Predicted Price: ${prediction[0]:,.2f}")
    else:
        study_hours = st.slider("Study Hours", 0, 10)
        attendance = st.slider("Attendance (%)", 0, 100)
        if st.button("Predict Score"):
            model = joblib.load("models/student_model.pkl")
            prediction = model.predict([[study_hours, attendance]])
            st.success(f"Predicted Score: {prediction[0]:.2f}")

