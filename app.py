import streamlit as st
import pdfplumber
from docx import Document
from langdetect import detect

st.set_page_config(page_title="Contract Analysis Bot")

st.title("📄 Contract Analysis Bot")

uploaded_file = st.file_uploader(
    "Upload contract (PDF or DOCX)",
    type=["pdf", "docx"]
)

def extract_text(file):
    if file.name.endswith(".pdf"):
        text = ""
        with pdfplumber.open(file) as pdf:
            for page in pdf.pages:
                text += page.extract_text() or ""
        return text

    elif file.name.endswith(".docx"):
        doc = Document(file)
        return "\n".join(p.text for p in doc.paragraphs)

if uploaded_file:
    contract_text = extract_text(uploaded_file)

    st.subheader("📑 Extracted Text")
    st.text_area("", contract_text, height=250)

    try:
        language = detect(contract_text)
        st.success(f"Detected Language: {language}")
    except:
        st.warning("Language detection failed")
