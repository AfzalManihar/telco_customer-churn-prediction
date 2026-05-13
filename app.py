import streamlit as st
import pickle
import numpy as np

# Load trained model
model = pickle.load(open("random_forest_model.pkl", "rb"))

# ================= TITLE =================

st.title("Telco Customer Churn Prediction")

st.write("Enter Customer Details Below")

# ================= INPUTS =================

gender = st.selectbox("Gender", ["Male", "Female"])

senior = st.selectbox("Senior Citizen", [0, 1])

partner = st.selectbox("Partner", ["Yes", "No"])

dependents = st.selectbox("Dependents", ["Yes", "No"])

tenure = st.number_input("Tenure", min_value=0)

phone_service = st.selectbox(
    "Phone Service",
    ["Yes", "No"]
)

multiple_lines = st.selectbox(
    "Multiple Lines",
    ["Yes", "No", "No phone service"]
)

online_security = st.selectbox(
    "Online Security",
    ["Yes", "No", "No internet service"]
)

online_backup = st.selectbox(
    "Online Backup",
    ["Yes", "No", "No internet service"]
)

device_protection = st.selectbox(
    "Device Protection",
    ["Yes", "No", "No internet service"]
)

tech_support = st.selectbox(
    "Tech Support",
    ["Yes", "No", "No internet service"]
)

streaming_tv = st.selectbox(
    "Streaming TV",
    ["Yes", "No", "No internet service"]
)

streaming_movies = st.selectbox(
    "Streaming Movies",
    ["Yes", "No", "No internet service"]
)

paperless_billing = st.selectbox(
    "Paperless Billing",
    ["Yes", "No"]
)

monthly_charges = st.number_input(
    "Monthly Charges",
    min_value=0.0
)

total_charges = st.number_input(
    "Total Charges",
    min_value=0.0
)

internet_service = st.selectbox(
    "Internet Service",
    ["DSL", "Fiber optic", "No"]
)

contract = st.selectbox(
    "Contract",
    ["Month-to-month", "One year", "Two year"]
)

payment_method = st.selectbox(
    "Payment Method",
    [
        "Bank transfer (automatic)",
        "Credit card (automatic)",
        "Electronic check",
        "Mailed check"
    ]
)

# ================= PREDICTION =================

if st.button("Predict"):

    # ===== Label Encoding =====

    gender = 1 if gender == "Male" else 0

    partner = 1 if partner == "Yes" else 0

    dependents = 1 if dependents == "Yes" else 0

    phone_service = 1 if phone_service == "Yes" else 0

    multiple_lines = 1 if multiple_lines == "Yes" else 0

    online_security = 1 if online_security == "Yes" else 0

    online_backup = 1 if online_backup == "Yes" else 0

    device_protection = 1 if device_protection == "Yes" else 0

    tech_support = 1 if tech_support == "Yes" else 0

    streaming_tv = 1 if streaming_tv == "Yes" else 0

    streaming_movies = 1 if streaming_movies == "Yes" else 0

    paperless_billing = 1 if paperless_billing == "Yes" else 0

    # ===== One-Hot Encoding =====

    internet_dsl = 1 if internet_service == "DSL" else 0
    internet_fiber = 1 if internet_service == "Fiber optic" else 0
    internet_no = 1 if internet_service == "No" else 0

    contract_month = 1 if contract == "Month-to-month" else 0
    contract_one = 1 if contract == "One year" else 0
    contract_two = 1 if contract == "Two year" else 0

    payment_bank = 1 if payment_method == "Bank transfer (automatic)" else 0
    payment_credit = 1 if payment_method == "Credit card (automatic)" else 0
    payment_electronic = 1 if payment_method == "Electronic check" else 0
    payment_mailed = 1 if payment_method == "Mailed check" else 0

    # ===== Final Input Array =====

    input_data = np.array([[
        gender,
        senior,
        partner,
        dependents,
        tenure,
        phone_service,
        multiple_lines,
        online_security,
        online_backup,
        device_protection,
        tech_support,
        streaming_tv,
        streaming_movies,
        paperless_billing,
        monthly_charges,
        total_charges,
        internet_dsl,
        internet_fiber,
        internet_no,
        contract_month,
        contract_one,
        contract_two,
        payment_bank,
        payment_credit,
        payment_electronic,
        payment_mailed
    ]])

    # ===== Prediction =====

    prediction = model.predict(input_data)

    # ===== Output =====

    if prediction[0] == 1:
        st.error("Customer Will Churn")

    else:
        st.success("Customer Will Stay")