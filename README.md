# 🛡️ AI-Powered Phishing Email Detector

An intelligent phishing detection system built with Machine Learning and 
adversarial testing using Google Gemini AI.

## 🔗 Live Demo
👉 [Click here to try it live](YOUR_STREAMLIT_LINK_HERE)

## 📊 Project Results
- ✅ Trained on **82,486 real emails**
- ✅ Achieved **98% detection accuracy**
- ✅ Conducted adversarial testing with **Gemini AI**
- ✅ Identified **45% evasion rate** on spear phishing emails
- ✅ Retrained model on adversarial samples

## 🧠 How It Works
1. User pastes any email into the dashboard
2. TF-IDF converts email text into numbers
3. Logistic Regression model predicts phishing probability
4. Dashboard shows verdict — Safe / Suspicious / Phishing

## ⚔️ Adversarial Testing
Used Google Gemini AI to generate smart phishing emails 
designed to evade detection. Found that casual spear phishing 
style emails (colleague document sharing) achieve 45% evasion 
rate — a finding that mirrors real enterprise SOC challenges.

## 🛠️ Tools Used
- Python, Scikit-learn, Pandas
- TF-IDF Vectorizer + Logistic Regression
- Google Gemini AI (adversarial email generation)
- Streamlit (dashboard + deployment)

## 📁 Project Structure
- app.py — Streamlit dashboard
- phishing_model_final.pkl — trained AI model
- vectorizer_final.pkl — text vectorizer
- requirements.txt — dependencies

## 👤 Author
**Bala Bhargav Murthy Ellapu**
Cybersecurity Enthusiast | SOC L1 Aspirant
