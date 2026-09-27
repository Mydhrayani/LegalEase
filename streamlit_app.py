import streamlit as st
import requests

st.title("LegalEase: AI-Powered Legal Document Generator")
doc_type = st.text_input("Document Type")
parties = st.text_input("Parties Involved")
terms = st.text_area("Terms and Conditions")
date = st.date_input("Effective Date")

if st.button("Generate Document"):
    st.write("Document Preview will appear here")
    st.write(f"Generating {doc_type} for {parties}")

st.markdown("Features: Document Preview, Editing, Downloads (TXT/DOCX/PDF)")
