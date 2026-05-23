from pydantic import BaseModel

class ExtractedData(BaseModel):
    name: str
    email: str
    subject: str
    summary: str

class EnrichedData(BaseModel):
    name: str
    email: str
    company: str
    linkedin_score: float
    summary: str
