import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Heart Disease Predictor",
    page_icon="❤️",
    layout="wide"
)

st.title("❤️ Heart Disease Risk Predictor")
st.write("This AI model predicts the **10-year risk of heart disease** based on health parameters.")

# Load dataset
@st.cache_data
def load_data():
    df = pd.read_csv("heart_disease.csv")
    df.fillna(0, inplace=True)
    return df

df = load_data()

# Train model
X = df.drop("TenYearCHD", axis=1)
y = df["TenYearCHD"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

accuracy = accuracy_score(y_test, model.predict(X_test))

st.sidebar.header("ℹ️ Model Info")
st.sidebar.write(f"Model Accuracy: **{round(accuracy*100,2)}%**")

# User Inputs
st.header("Enter Your Health Details")

col1, col2, col3 = st.columns(3)

with col1:
    age = st.slider("Age", 18, 100, 40)
    education = st.slider("Education Level", 0, 4, 2)
    male = st.selectbox("Gender", ["Female", "Male"])

with col2:
    currentSmoker = st.selectbox("Current Smoker", ["No", "Yes"])
    cigsPerDay = st.slider("Cigarettes Per Day", 0, 70, 0)
    BPMeds = st.selectbox("BP Medication", ["No", "Yes"])

with col3:
    prevalentStroke = st.selectbox("Previous Stroke", ["No", "Yes"])
    prevalentHyp = st.selectbox("Hypertension", ["No", "Yes"])
    diabetes = st.selectbox("Diabetes", ["No", "Yes"])

st.subheader("Clinical Measurements")

col4, col5, col6 = st.columns(3)

with col4:
    totChol = st.slider("Total Cholesterol", 100, 600, 200)

with col5:
    sysBP = st.slider("Systolic BP", 80, 250, 120)
    diaBP = st.slider("Diastolic BP", 40, 150, 80)

with col6:
    BMI = st.slider("BMI", 15.0, 50.0, 25.0)
    heartRate = st.slider("Heart Rate", 40, 200, 70)
    glucose = st.slider("Glucose", 40, 400, 90)

# Convert inputs
male = 1 if male == "Male" else 0
currentSmoker = 1 if currentSmoker == "Yes" else 0
BPMeds = 1 if BPMeds == "Yes" else 0
prevalentStroke = 1 if prevalentStroke == "Yes" else 0
prevalentHyp = 1 if prevalentHyp == "Yes" else 0
diabetes = 1 if diabetes == "Yes" else 0

# Prediction
if st.button("🔍 Predict Heart Disease Risk"):

    input_data = np.array([[male, age, education, currentSmoker, cigsPerDay,
                            BPMeds, prevalentStroke, prevalentHyp, diabetes,
                            totChol, sysBP, diaBP, BMI, heartRate, glucose]])

    prob = model.predict_proba(input_data)[0][1]
    risk = round(prob * 100, 2)

    st.subheader("Prediction Result")

    st.metric("Heart Disease Risk", f"{risk}%")

    if risk < 15:
        st.success("Low Risk ❤️")
    elif risk < 30:
        st.warning("Moderate Risk ⚠️")
    else:
        st.error("High Risk 🚨 Please consult a doctor")

    # Chart
    st.subheader("Risk Visualization")

    fig, ax = plt.subplots()

    labels = ["Risk", "Safe"]
    values = [risk, 100 - risk]

    ax.pie(values, labels=labels, autopct="%1.1f%%", startangle=90)
    ax.axis("equal")

    st.pyplot(fig)

# Dataset preview
st.subheader("Dataset Preview")
st.dataframe(df.head())

st.caption("⚠️ This tool is for educational purposes only. Always consult a healthcare professional.")