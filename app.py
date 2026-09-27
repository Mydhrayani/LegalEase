import streamlit as st
import requests
from formatter import sanitize_text, format_html_preview, format_docx, format_pdf

WEB_LOGO_PATH = "https://via.placeholder.com/300x100?text=LegalEase"

st.set_page_config(page_title="LegalEase", layout="centered")
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.image(WEB_LOGO_PATH, use_container_width=True)

st.markdown("<h2 style='text-align: center;'>AI Legal Document Generator</h2>", unsafe_allow_html=True)

document_type = st.text_input("document_type")
parties = st.text_area("parties")
terms = st.text_area("terms")
dates = st.text_input("dates")

if st.button("Generate Document"):
    response = requests.post("http://localhost:8000/generate", json={"document_type": document_type, "parties": parties, "terms": terms, "dates": dates})
    generated_text = sanitize_text(response.json()["document"])
    styled_html = format_html_preview(generated_text)
    st.markdown(styled_html, unsafe_allow_html=True)
    edited_text = st.text_area("Edit Document Below:", generated_text, height=300)
    st.download_button("📄 Download as .TXT", data=generated_text, file_name=f"{document_type.replace(' ', '_').lower()}_document.txt")
    st.download_button("📝 Download as .DOCX", data=format_docx(generated_text, document_type), file_name=f"{document_type.replace(' ', '_').lower()}_document.docx")
    st.download_button("📕 Download as .PDF", data=format_pdf(generated_text, document_type), file_name=f"{document_type.replace(' ', '_').lower()}_document.pdf")
