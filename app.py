import streamlit as st
import requests

st.set_page_config(
    page_title="ReliefReady AI",
    page_icon="🏛️",
    layout="wide"
)

N8N_FORM_URL = "https://hackathonproject09.app.n8n.cloud/form/9b144957-b00a-4d34-a214-a3d0626f3911"

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
        with st.spinner("Sending document for AI analysis..."):

            files = {
                "Government_Document": (
                    uploaded_file.name,
                    uploaded_file.getvalue(),
                    uploaded_file.type
                )
            }

            data = {
                "Case ID": "WEB-" + uploaded_file.name,
                "Document Name": uploaded_file.name,
                "Person Type": "Not specified",
                "Location": "Not specified",
                "Document Type": "Government Notice"
            }

            response = requests.post(
                N8N_FORM_URL,
                data=data,
                files=files,
                timeout=60
            )

            if response.ok:
                st.success("✅ Document submitted successfully!")
                st.info(
                    "ReliefReady AI is now analyzing your document."
                )
            else:
                st.error(
                    f"❌ Unable to submit document. "
                    f"Status code: {response.status_code}"
                )
