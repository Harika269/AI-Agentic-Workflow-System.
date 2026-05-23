from app.agent import extract_data
from app.enrich import enrich_record
from app.evaluator import validate_record
from app.vectorstore import build_vectorstore

def run_pipeline(text: str):
    vectordb = build_vectorstore()

    extracted = extract_data(text)
    enriched = enrich_record(extracted)
    validate_record(enriched)

    return enriched
