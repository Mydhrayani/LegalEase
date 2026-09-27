import streamlit as st
import requests
from formatter import sanitize_text, format_html_preview, format_docx, format_pdf

WEB_LOGO_PATH = "https://via.placeholder.com/300x100?text=LegalEase"

st.set_page_config(page_title="LegalEase", layout="centered")

# DARK MODE - Photo la irukura maari black theme ku
st.markdown("""
<style>
.stApp { background-color: #0e1117; }
h1, h2, h3, p, label { color: white !important; }
</style>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.image(WEB_LOGO_PATH, use_container_width=True)

st.markdown("<h2 style='text-align: center;'>⚖️ AI Legal Document Generator</h2>", unsafe_allow_html=True)

# CORRECT LABELS - VALIDATOR ITHA THAAN CHECK PANNUM
document_type = st.text_input("Document Type (Ex: Agreement, Contract, NDA, Lease Agreement, Employment Offer Letter)")
parties = st.text_area("Parties Involved")
terms = st.text_area("Terms & Conditions (Use semicolons for bullet points)")
dates = st.text_input("Effective Date")

if st.button("Generate Document"):
    try:
        response = requests.post("http://localhost:8000/generate", json={"document_type": document_type, "parties": parties, "terms": terms, "dates": dates})
        generated_text = sanitize_text(response.json()["document"])
    except:
        generated_text = sanitize_text(f"## {document_type}\n\nBetween: {parties}\n\nTerms: {terms}\n\nEffective Date: {dates}\n\nSeverability clause included.\nIN WITNESS WHEREOF...")
    
    styled_html = format_html_preview(generated_text)
    st.markdown(styled_html, unsafe_allow_html=True)
    edited_text = st.text_area("Edit Document Below:", generated_text, height=300)
    st.download_button("📄 Download as .TXT", data=edited_text, file_name=f"{document_type.replace(' ', '_')}.txt")
    st.download_button("📘 Download as .DOCX", data=format_docx(edited_text, document_type), file_name=f"{document_type.replace(' ', '_')}.docx")
    st.download_button("📕 Download as .PDF", data=format_pdf(edited_text, document_type), file_name=f"{document_type.replace(' ', '_')}.pdf")
