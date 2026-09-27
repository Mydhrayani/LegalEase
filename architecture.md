# Architecture - LegalEase Legal Document Generator

Frontend: React form - collects Document Type, Parties, Terms, Dates
Backend: Node.js Express API - /api/generate endpoint
AI Layer: Google Generative AI SDK - gemini-1.5-pro
Flow: User Input -> Prompt Builder -> Gemini API -> Parsed Legal Document -> Download

Components:
- React UI with 4 inputs
- Express validation
- Prompt template: "Generate {type} for {parties} with {terms} from {date}"
- Gemini 1.5 Pro generation with 1M token context

Tech: React, Node.js, @google/generative-ai
