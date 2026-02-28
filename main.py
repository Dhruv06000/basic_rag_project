# main.py

from src.load_data import load_documents
from src.chunk import chunk_text
from config import DOC_PATH, CHUNK_SIZE, OVERLAP

# Step 1: Load documents
documents = load_documents(DOC_PATH)
print(f"Loaded {len(documents)} documents.")

# Optional: Preview first 2 documents (for debugging)
# for doc in documents[:2]:
#     print(doc["filename"])
#     print(doc["content"][:100], "...")  # first 100 characters

# Step 2: Chunk documents
all_chunks = []

for doc in documents:
    text = doc["content"]  # your document text
    chunks = chunk_text(text, chunk_size=CHUNK_SIZE, overlap_fraction=OVERLAP)
    all_chunks.extend(chunks)

print(f"Total chunks created: {len(all_chunks)}")

# Optional: Preview first 5 chunks
for i, chunk in enumerate(all_chunks[:5]):
    print(f"Chunk {i+1}:\n{chunk}\n---")

# Step 3: Save chunks for future embedding (optional)
# import pickle
# with open("all_chunks.pkl", "wb") as f:
#     pickle.dump(all_chunks, f)
# print("Chunks saved to all_chunks.pkl")