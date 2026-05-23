# AI-Agentic-Workflow-System.
Production-grade AI agentic workflow that automates document → JSON extraction, enrichment, RAG search, and validation using multi-step LLM agents, FAISS vector search, structured output parsing, retries, and fault-tolerant pipelines.
# AI Agentic Workflow – Document Automation + Enrichment + RAG

This project implements a production-grade AI agent built with Python, LangChain-style orchestration, vector search, structured extraction, validation, and automated enrichment.  

It performs:

✔ PDF/Document → JSON extraction  
✔ Enrichment with external APIs (rate-limit safe)  
✔ RAG-based answer generation  
✔ Guardrail validation + schema enforcement  
✔ Agent reasoning with retries & fallbacks  
✔ End-to-end pipeline automation  

This repo showcases engineering patterns used in real-world LLM applications.

---

## 🧩 Features

- Multi-step LLM agent (reasoning + tool use)
- Vector database pipeline (FAISS)
- Structured output (Pydantic schemas)
- Automatic enrichment API calls + retry logic
- Validation, guardrails, and error handling
- Modular pipeline with full observability

---

## 🚀 Run the Pipeline

```bash
pip install -r requirements.txt
python app/main.py
