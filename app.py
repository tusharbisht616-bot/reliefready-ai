import streamlit as st
import requests
N8N_FORM_URL = "https://hackathonproject09.app.n8n.cloud/form-test/9b144957-b00a-4d34-a214-a3d0626f3911"
st.set_page_config(
    page_title="ReliefReady AI",
    page_icon="🏛️",
    layout="wide"
)

st.title("🏛️ ReliefReady AI")
st.subheader("From confusing government notice to clear action in seconds.")

st.write(
    "Upload a government welfare document and get a clear, "
    "structured action plan."
)

uploaded_file = st.file_uploader(
    "Upload Government Document",
    type=["pdf"]
)

if uploaded_file:
    st.success(f"Document uploaded: {uploaded_file.name}")

    if st.button("🔍 Analyze Document", type="primary"):
        st.info("AI analysis started...")
