from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from app.schemas import ExtractedData

prompt = PromptTemplate.from_template("""
Extract the following fields from the text:
- name
- email
- subject
- summary (short)

TEXT:
{content}

Return JSON only.
""")

def extract_data(content: str) -> ExtractedData:
    llm = OpenAI(temperature=0)
    output = llm(prompt.format(content=content))
    return ExtractedData.parse_raw(output)
