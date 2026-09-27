from fastapi import FastAPI
from gemini_generator import generate_legal_doc
from pydantic import BaseModel

app = FastAPI()

class DocRequest(BaseModel):
    doc_type: str
    parties: str
    terms: str
    effective_date: str

@app.post("/generate")
def generate(data: DocRequest):
    result = generate_legal_doc(data.doc_type, data.parties, data.terms, data.effective_date)
    return {"document": result}

@app.get("/")
def home():
    return {"message": "LegalEase API Running"}
