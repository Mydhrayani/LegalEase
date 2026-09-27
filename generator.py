import google.generativeai as genai
import os

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel('gemini-1.5-pro')

def generate_legal_doc(doc_type, parties, terms, effective_date):
    prompt = f"""Generate a formal {doc_type} between {parties} 
    with terms: {terms} effective from {effective_date}.
    Include Title, Parties, Terms, Signature sections. Use legal jargon.
    Generate output suitable for TXT, DOCX, PDF formatting."""
    response = model.generate_content(prompt)
    return response.text
