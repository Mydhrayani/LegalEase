from io import BytesIO
import re

def sanitize_text(text):
    return re.sub(r'[^\x00-\x7F]+', '', text)

def format_html_preview(text):
    return f"<div style='padding:15px'><pre>{text}</pre></div>"

def format_docx(text, doc_type):
    from docx import Document
    doc = Document()
    doc.add_heading(doc_type, 0)
    doc.add_paragraph(text)
    bio = BytesIO()
    doc.save(bio)
    return bio.getvalue()

def format_pdf(text, doc_type):
    from fpdf import FPDF
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, text)
    return pdf.output(dest='S').encode('latin-1')
