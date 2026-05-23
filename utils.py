import time
import requests
from tenacity import retry, stop_after_attempt, wait_exponential

@retry(stop=stop_after_attempt(5), wait=wait_exponential(multiplier=2))
def safe_enrich_api(email: str):
    # Fake enrichment API placeholder
    time.sleep(0.1)
    return {
        "company": "Example Corp",
        "linkedin_score": 87.5
    }
