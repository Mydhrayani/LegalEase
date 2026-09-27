from fastapi import APIRouter
from pydantic import BaseModel
from gemini_generator import generate_legal_document

router = APIRouter()

class DocumentRequest(BaseModel):
    document_type: str
    parties: str
    terms: str
    dates: str

@router.post("/generate")
def generate(request: DocumentRequest):
    result = generate_legal_document(request.document_type, request.parties, request.terms, request.dates)
    return {"document": result}
