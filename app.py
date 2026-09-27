import streamlit as st
import requests
from formatter import format_docx, format_pdf, format_html_preview

# 3. User Interaction
st.title("LegalEase: AI-Powered Legal Document Generator")
document_type = st.text_input("Document Type")
parties = st.text_input("Parties Involved")
terms = st.text_area("Terms and Conditions")
dates = st.text_input("Effective Date")

if "generated_text" not in st.session_state:
    st.session_state.generated_text = "Sample Legal Document"
if "show_edit" not in st.session_state:
    st.session_state.show_edit = True

if st.button("Generate Document"):
    # Send to backend
    try:
        response = requests.post("http://localhost:8000/generate", json={
            "document_type": document_type,
            "parties": parties,
            "terms": terms,
            "dates": dates
        })
        st.session_state.generated_text = response.json().get("document", "Generated")
    except:
        st.session_state.generated_text = f"Generated {document_type} for {parties}"
    st.session_state.show_edit = True

generated_text = st.session_state.generated_text

# 4. Editable Document & Download
if st.session_state.get("show_edit"):
    edited_text = st.text_area("Edit Document Below:", generated_text, height=300)
    st.session_state.generated_text = edited_text
    generated_text = edited_text
    st.download_button("📄 Download as .TXT", data=generated_text, file_name="doc.txt")
    st.download_button("📝 Download as .DOCX", data=format_docx(generated_text, document_type), file_name="doc.docx")
    st.download_button("📕 Download as .PDF", data=format_pdf(generated_text, document_type), file_name="doc.pdf")
    st.markdown(format_html_preview(generated_text), unsafe_allow_html=True)
