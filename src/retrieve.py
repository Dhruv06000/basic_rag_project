import numpy as np
import pickle
import os
from sklearn.metrics.pairwise import cosine_similarity
from config import PROCESSED_PATH, EMBEDDINGS_FILE, CHUNKS_FILE

def retrieve(query_embedding, top_k=5):

    embeddings = np.load(os.path.join(PROCESSED_PATH, EMBEDDINGS_FILE))

    with open(os.path.join(PROCESSED_PATH, CHUNKS_FILE), "rb") as f:
        chunks = pickle.load(f)

    scores = cosine_similarity([query_embedding], embeddings)[0]

    top_indices = np.argsort(scores)[-top_k:][::-1]
    
    results = [(chunks[i], scores[i]) for i in top_indices]
    return results
