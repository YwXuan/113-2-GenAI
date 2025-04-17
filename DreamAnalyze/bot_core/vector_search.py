import faiss
import numpy as np
import pickle
from sentence_transformers import SentenceTransformer

# 載入模型與向量資料庫
model = SentenceTransformer("paraphrase-multilingual-MiniLM-L12-v2")
index = faiss.read_index("vector_db/index.faiss")

with open("vector_db/index.pkl", "rb") as f:
    raw = pickle.load(f)
    if isinstance(raw, tuple):
        _, documents = raw
    else:
        documents = raw

documents = list(documents)
while len(documents) < index.ntotal:
    documents.append("（資料遺失）")

def search_similar_dreams(text: str, top_k=3):
    vec = model.encode([text]).astype("float32")
    D, I = index.search(vec, top_k)
    return [documents[i] for i in I[0] if i < len(documents)]