# 💳 Fraud Detection Prediction App

A machine learning web application built with **Streamlit** and **Logistic Regression** to predict whether a financial transaction is **fraudulent or legitimate**.  
This app demonstrates an end-to-end ML workflow — from data preprocessing and model training to deployment on Streamlit Cloud.

---

## 🚀 Features
- 🧠 **Machine Learning Model** – Logistic Regression trained on 1.9M+ transactions.  
- ⚖️ **Handles Class Imbalance** using `class_weight='balanced'`.  
- 🎨 **Modern Streamlit UI** with interactive input fields and styled results.  
- 📈 **Prediction with Confidence Score** (fraud probability).  
- 💾 **Reusable Model** saved and loaded using `joblib`.  
- ☁️ **Deployed on Streamlit Cloud** for instant access.

---

## 🧩 Tech Stack
- **Python 3.12**
- **Streamlit** – for building the interactive web interface  
- **Pandas** – for data manipulation  
- **Scikit-learn 1.6.1** – for model training and pipeline  
- **Joblib** – for saving and loading the trained model  

---

## ⚙️ Installation & Setup (Local)

1. **Clone the repository**
   ```bash
   git clone https://github.com/sajivanK/fraud-detection.git
   cd fraud-detection-app
   ```

2. **Create a virtual environment (recommended)**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # Mac/Linux
   .venv\Scripts\activate     # Windows
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Streamlit app**
   ```bash
   streamlit run fraud_detection.py
   ```

---

## 🧠 How It Works

1. The user inputs transaction details:
   - Type (`PAYMENT`, `TRANSFER`, `CASH_OUT`, `DEPOSIT`)
   - Amount
   - Sender and Receiver balances before & after the transaction

2. The app feeds this data into a **Logistic Regression pipeline** trained with:
   - Feature scaling (`StandardScaler`)
   - One-hot encoding for transaction type
   - Class imbalance correction (`class_weight='balanced'`)

3. The model predicts whether the transaction is **fraudulent (1)** or **legitimate (0)** and displays:
   - Fraud probability
   - A styled message (red for fraud, green for safe)

---

## 📊 Model Overview

| Metric | Result |
|---------|---------|
| **Accuracy** | 94% |
| **Recall (Fraud)** | 0.94 |
| **Precision (Fraud)** | Lower (due to high imbalance) |
| **Algorithm** | Logistic Regression |

---

## 📁 Project Structure

```
📦 fraud-detection-app
├── fraud_detection.py         # Streamlit web app
├── fraud_detection_model.pkl  # Trained ML model
├── AIML Dataset.csv           # Dataset (optional for retraining)
├── requirements.txt           # Dependencies
└── README.md                  # Project documentation
```

---

## ☁️ Deployment on Streamlit Cloud

1. Push this repository to GitHub.  
2. Go to [[https://share.streamlit.io](https://fraud-detection-btdzhenb7f2sbqibe3ojcq.streamlit.app/)].  
3. Click **New app → Connect your GitHub repo**.  
4. Select `fraud_detection.py` as the main file.  
5. Streamlit Cloud will automatically install the packages from `requirements.txt`.  
6. Done! 🎉 Your app is live.

---

## 🧾 Example Use

**Input Example:**
- Type: `TRANSFER`  
- Amount: `1000`  
- Sender Old Balance: `10000`  
- Sender New Balance: `9000`  
- Receiver Old Balance: `0`  
- Receiver New Balance: `0`

**Output:**
> ⚠️ Fraudulent Transaction Detected  
> Probability of Fraud: **78.42%**

---

## ✨ Author
**Sajivan Kunarethinam**  
_Data Science Student | Machine Learning Enthusiast_  

---

## 🛠️ Future Improvements
- Add advanced models like **LightGBM** or **XGBoost**  
- Integrate fraud probability visualization  
- Add API endpoint for external systems  

---

## 📜 License
This project is open-source and available under the [MIT License](LICENSE).
