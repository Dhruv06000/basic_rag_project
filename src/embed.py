import pickle
import os
import numpy as np
from sentence_transformers import SentenceTransformer
from config import PROCESSED_PATH, CHUNKS_FILE, EMBEDDINGS_FILE, EMBEDDING_MODEL


# Load embedding model
model = SentenceTransformer(EMBEDDING_MODEL)


def embed_chunks():
    """Generate embeddings for stored chunks and save them."""

    chunks_path = os.path.join(PROCESSED_PATH, CHUNKS_FILE)

    with open(chunks_path, "rb") as f:
        all_chunks = pickle.load(f)

    print(f"Loaded {len(all_chunks)} chunks.")

    chunk_embeddings = model.encode(
        all_chunks,
        show_progress_bar=True,
        normalize_embeddings=True
    )

    embeddings_path = os.path.join(PROCESSED_PATH, EMBEDDINGS_FILE)

    np.save(embeddings_path, chunk_embeddings)

    print("Chunk embeddings saved ✅")
    print(f"Embedding shape: {chunk_embeddings.shape}")


def embed_query(query: str):
    """Create embedding for user query."""
    
    query_embedding = model.encode(
        query,
        normalize_embeddings=True
    )

    return query_embedding