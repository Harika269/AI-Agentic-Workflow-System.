from app.pipeline import run_pipeline

def test_pipeline():
    output = run_pipeline("John Doe emailed about product pricing.")
    assert output.name != ""
    assert output.linkedin_score > 0
