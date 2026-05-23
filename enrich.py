from app.utils import safe_enrich_api
from app.schemas import EnrichedData

def enrich_record(extracted):
    enriched = safe_enrich_api(extracted.email)
    return EnrichedData(
        name=extracted.name,
        email=extracted.email,
        company=enriched["company"],
        linkedin_score=enriched["linkedin_score"],
        summary=extracted.summary
    )
