import faiss
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS

def build_vectorstore():
    with open("data/knowledge_base.txt") as f:
        docs = f.readlines()

    embeddings = OpenAIEmbeddings()
    return FAISS.from_texts(docs, embeddings)
