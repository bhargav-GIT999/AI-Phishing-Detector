import streamlit as st
import pickle
import time

# Load model and vectorizer
with open("phishing_model_final.pkl", "rb") as f:
    model = pickle.load(f)

with open("vectorizer_final.pkl", "rb") as f:
    vectorizer = pickle.load(f)

# Page config
st.set_page_config(
    page_title="AI Phishing Detector",
    page_icon="🛡️",
    layout="centered"
)

# Header
st.title("🛡️ AI Phishing Email Detector")
st.markdown("Built by **Bala Bhargav Murthy Ellapu** — Cybersecurity Portfolio Project")
st.markdown("---")

# Input
st.subheader("📧 Paste Email Content Below")
email_input = st.text_area(
    "Email text:",
    height=250,
    placeholder="Paste the full email content here including subject, body..."
)

# Analyze button
if st.button("🔍 Analyze Email", use_container_width=True):
    if email_input.strip() == "":
        st.warning("⚠️ Please paste an email first.")
    else:
        with st.spinner("Analyzing..."):
            time.sleep(1)
            vec = vectorizer.transform([email_input])
            prob = model.predict_proba(vec)[0]
            safe_prob = prob[0] * 100
            phishing_prob = prob[1] * 100

        st.markdown("---")
        st.subheader("📊 Analysis Results")

        # Show meter
        col1, col2 = st.columns(2)
        with col1:
            st.metric("✅ Safe Probability", f"{safe_prob:.1f}%")
        with col2:
            st.metric("⚠️ Phishing Probability", f"{phishing_prob:.1f}%")

        # Progress bar
        st.progress(int(phishing_prob))

        # Verdict
        st.markdown("---")
        if phishing_prob >= 80:
            st.error("🚨 HIGH RISK — Very likely phishing. Do NOT click any links.")
        elif phishing_prob >= 50:
            st.warning("⚠️ MEDIUM RISK — Suspicious email. Verify before clicking.")
        else:
            st.success("✅ LOW RISK — Email appears legitimate.")

        # Details
        with st.expander("🔬 See detailed breakdown"):
            st.write(f"**Phishing score:** {phishing_prob:.2f}%")
            st.write(f"**Safe score:** {safe_prob:.2f}%")
            if phishing_prob >= 80:
                st.write("**Reason:** High concentration of phishing indicators detected.")
            elif phishing_prob >= 50:
                st.write("**Reason:** Some suspicious patterns found — proceed with caution.")
            else:
                st.write("**Reason:** No significant phishing patterns detected.")

st.markdown("---")
st.caption("⚡ Powered by Logistic Regression + TF-IDF | Adversarial tested with Gemini AI")