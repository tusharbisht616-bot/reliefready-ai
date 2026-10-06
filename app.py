import streamlit as st

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

    st.info(
        "Your document is ready for AI analysis. "
        "The AI analysis connection will be added next."
    )
