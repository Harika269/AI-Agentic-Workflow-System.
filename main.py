import json
from app.pipeline import run_pipeline

if __name__ == "__main__":
    with open("data/sample_input.json") as f:
        data = json.load(f)

    result = run_pipeline(data["content"])
    print(result.json(indent=2))
