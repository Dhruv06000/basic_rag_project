from src.load_data import load_documents
from src.chunk import chunk_text
from src.embed import embed_chunks
from config import DOC_PATH, CHUNK_SIZE, OVERLAP

import pickle
import os

# Step 1: Load documents
documents = load_documents(DOC_PATH)
print(f"Loaded {len(documents)} documents")

# Step 2: Chunk documents
all_chunks = []

for doc in documents:
    chunks = chunk_text(
        doc["content"],
        chunk_size=CHUNK_SIZE,
        overlap_fraction=OVERLAP
    )
    all_chunks.extend(chunks)

print(f"Created {len(all_chunks)} chunks")

# Step 3: Save chunks
os.makedirs("data/processed", exist_ok=True)

with open("data/processed/all_chunks.pkl", "wb") as f:
    pickle.dump(all_chunks, f)

print("Chunks saved")

# Step 4: Create embeddings
embed_chunks()

print("Index built successfully")