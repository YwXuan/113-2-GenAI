import pickle
with open('vector_db/index.pkl', 'rb') as f:
    docs = pickle.load(f)
print(len(docs))  # ← 這要跟 index 裡面一樣多

import faiss
idx = faiss.read_index('vector_db/index.faiss')
print(idx.ntotal)  # ← 應該要等於 len(docs)
