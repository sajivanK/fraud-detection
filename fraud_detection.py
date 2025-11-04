import streamlit as st
import pandas as pd
import joblib

# ======================
# Load the trained model
# ======================
model = joblib.load("fraud_detection_model.pkl")

# ======================
# Page Configuration
# ======================
st.set_page_config(
    page_title="Fraud Detection App",
    page_icon="💳",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ======================
# Custom CSS styling
# ======================
st.markdown("""
    <style>
    body {
        background-color: #F8F9FB;
    }
    .stApp {
        background: linear-gradient(135deg, #f5f7fa, #c3cfe2);
        padding: 2rem;
        border-radius: 15px;
    }
    .title {
        text-align: center;
        color: #1E3D58;
        font-size: 2.2rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
    }
    .subtitle {
        text-align: center;
        color: #4F6D7A;
        font-size: 1rem;
        margin-bottom: 2rem;
    }
    .result-box {
        background-color: white;
        padding: 1.5rem;
        border-radius: 12px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        text-align: center;
    }
    .fraud {
        background-color: #ffe6e6;
        color: #c0392b;
        border-left: 8px solid #c0392b;
    }
    .legit {
        background-color: #e9f7ef;
        color: #1e8449;
        border-left: 8px solid #1e8449;
    }
    </style>
""", unsafe_allow_html=True)

# ======================
# Header Section
# ======================
st.markdown('<div class="title">💳 Fraud Detection Prediction App</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Enter transaction details below and click <b>Predict</b> to check if it may be fraudulent.</div>', unsafe_allow_html=True)

st.divider()

# ======================
# Input Section
# ======================
col1, col2 = st.columns(2)

with col1:
    transaction_type = st.selectbox("Transaction Type", ["PAYMENT", "TRANSFER", "CASH_OUT", "DEPOSIT"])
    amount = st.number_input("💰 Transaction Amount", min_value=0.0, value=1000.0)
    oldbalanceOrg = st.number_input("🏦 Old Balance (Sender)", min_value=0.0, value=10000.0)

with col2:
    newbalanceOrig = st.number_input("💳 New Balance (Sender)", min_value=0.0, value=9000.0)
    oldbalanceDest = st.number_input("🏁 Old Balance (Receiver)", min_value=0.0, value=0.0)
    newbalanceDest = st.number_input("💵 New Balance (Receiver)", min_value=0.0, value=0.0)

st.markdown("<br>", unsafe_allow_html=True)

# ======================
# Predict Button
# ======================
center_col = st.columns([1, 2, 1])[1]
with center_col:
    predict_btn = st.button("🔍 Predict Transaction", use_container_width=True)

# ======================
# Prediction Section
# ======================
if predict_btn:
    # Prepare input data
    input_data = pd.DataFrame([{
        "type": transaction_type,
        "amount": amount,
        "oldbalanceOrg": oldbalanceOrg,
        "newbalanceOrig": newbalanceOrig,
        "oldbalanceDest": oldbalanceDest,
        "newbalanceDest": newbalanceDest
    }])

    # Make prediction
    prediction = model.predict(input_data)[0]
    prob = model.predict_proba(input_data)[0][1]  # Probability of fraud

    # Display results
    if prediction == 1:
        st.markdown(
            f"""
            <div class="result-box fraud">
                <h3>⚠️ Fraudulent Transaction Detected</h3>
                <p>This transaction has a <b>{prob*100:.2f}%</b> probability of being <b>fraudulent</b>.</p>
            </div>
            """, unsafe_allow_html=True
        )
    else:
        st.markdown(
            f"""
            <div class="result-box legit">
                <h3>✅ Legitimate Transaction</h3>
                <p>This transaction appears to be <b>safe</b> with only <b>{prob*100:.2f}%</b> fraud likelihood.</p>
            </div>
            """, unsafe_allow_html=True
        )

    st.markdown("<br>", unsafe_allow_html=True)
    st.info("💡 Tip: In real-world fraud systems, thresholds can be tuned to balance false alarms and detection rates.")

