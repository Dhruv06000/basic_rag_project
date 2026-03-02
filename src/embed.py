import pickle
import os
import numpy as np
from sentence_transformers import SentenceTransformer
from config import PROCESSED_PATH, CHUNKS_FILE, EMBEDDINGS_FILE, MODEL_NAME


# Ensure processed folder exists
os.makedirs(PROCESSED_PATH, exist_ok=True)

# Load saved chunks
chunks_path = os.path.join(PROCESSED_PATH, CHUNKS_FILE)

with open(chunks_path, "rb") as f:
    all_chunks = pickle.load(f)

print(f"Loaded {len(all_chunks)} chunks.")

# Load model
model = SentenceTransformer(MODEL_NAME)

# Create normalized embeddings
chunk_embeddings = model.encode(
    all_chunks,
    show_progress_bar=True,
    normalize_embeddings=True
)

# Save embeddings
embeddings_path = os.path.join(
    PROCESSED_PATH,
    EMBEDDINGS_FILE
)

np.save(embeddings_path, chunk_embeddings)

print("Chunk embeddings saved ✅")
print(f"Embedding shape: {chunk_embeddings.shape}")