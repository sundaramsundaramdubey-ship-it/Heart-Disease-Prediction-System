
# ❤️ Heart Disease Risk Predictor

An interactive **Machine Learning web application** built with **Streamlit** that predicts the **10-year risk of coronary heart disease (CHD)** using health and lifestyle parameters.

This project uses **Logistic Regression** trained on the **Framingham Heart Study dataset** to estimate heart disease risk.

---

# 📊 Project Overview

Heart disease is one of the leading causes of death worldwide.
This application allows users to enter clinical and lifestyle data to estimate their **risk of developing heart disease within 10 years**.

The model analyzes multiple health factors such as:

* Age
* Blood pressure
* Cholesterol
* Smoking habits
* BMI
* Glucose level
* Diabetes status

The result is presented as a **risk percentage and risk category**.

---

# 🚀 Features

✅ User-friendly web interface using **Streamlit**
✅ Predicts **10-year heart disease risk**
✅ Displays **risk percentage**
✅ Shows **Low / Moderate / High risk classification**
✅ Interactive **visual chart of prediction**
✅ Trained using **Logistic Regression (Scikit-Learn)**
✅ Simple and clean dashboard layout

---

# 🧠 Machine Learning Model

**Algorithm Used**

* Logistic Regression

**Model Workflow**

1. Load dataset
2. Handle missing values
3. Split data into training and testing sets
4. Train Logistic Regression model
5. Evaluate model accuracy
6. Use model to predict user input risk

---

# 📂 Project Structure

```
HeartDiseasePredictor
│
├── app.py
├── heart_disease.csv
├── requirements.txt
└── README.md
```

---

# ⚙️ Installation

Clone the repository

```
git clone https://github.com/yourusername/HeartDiseasePredictor.git
```

Navigate to project folder

```
cd HeartDiseasePredictor
```

Install required libraries

```
pip install -r requirements.txt
```

---

# ▶️ Run the Application

Start the Streamlit server

```
streamlit run app.py
```

Open the app in your browser

```
http://localhost:8501
```

---

# 📈 Input Parameters

The prediction model uses the following health features:

* Age
* Gender
* Education Level
* Smoking Status
* Cigarettes Per Day
* Blood Pressure Medication
* Previous Stroke
* Hypertension
* Diabetes
* Total Cholesterol
* Systolic Blood Pressure
* Diastolic Blood Pressure
* Body Mass Index (BMI)
* Heart Rate
* Glucose Level

---

# 📊 Dataset

Dataset used: **Framingham Heart Study Dataset**

It contains medical records used to predict the **10-year risk of coronary heart disease**.

Number of records: **4,000+**

---

# 🛠 Technologies Used

* Python
* Streamlit
* Pandas
* NumPy
* Scikit-Learn
* Matplotlib

---

# 📌 Future Improvements

* SHAP Explainable AI
* Interactive Plotly dashboards
* Risk factor visualization
* Health report PDF download
* Model comparison (Random Forest, XGBoost)

---

# ⚠️ Disclaimer

This project is for **educational purposes only**.
It should **not be used for medical diagnosis**. Always consult a qualified healthcare professional.

---

# 👨‍💻 Author

**Manish Yadav**
Data Analyst

📧 [my45516gy@gmail.com](mailto:my45516gy@gmail.com)
📞 9005623641

---

⭐ If you found this project useful, please consider **starring the repository**.
