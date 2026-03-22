import numpy as np
import pickle
import os
from config import PROCESSED_PATH, EMBEDDINGS_FILE, CHUNKS_FILE, RETRIEVAL_TOP_K


# 📂 Load data once (global)

embeddings_path = os.path.join(PROCESSED_PATH, EMBEDDINGS_FILE)
chunks_path = os.path.join(PROCESSED_PATH, CHUNKS_FILE)

# Load embeddings
embeddings = np.load(embeddings_path)

# Load chunks
with open(chunks_path, "rb") as f:
    chunks = pickle.load(f)

print(f"Loaded {len(chunks)} chunks.")
print(f"Embedding shape: {embeddings.shape}")


#  Retrieval function

def retrieve(query_embedding, top_k=RETRIEVAL_TOP_K, with_scores=False):
    """
    Retrieve top-k most relevant chunks for a given query embedding.
    """

    # Ensure query is numpy array
    query_embedding = np.array(query_embedding)

    # Cosine similarity (since embeddings are normalized)
    scores = np.dot(embeddings, query_embedding)

    # Get top-k indices (highest scores first)
    top_indices = np.argsort(scores)[-top_k:][::-1]

    if with_scores:
        return [(chunks[i], float(scores[i])) for i in top_indices]

    return [chunks[i] for i in top_indices]