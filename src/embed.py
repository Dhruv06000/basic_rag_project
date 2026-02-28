import os
import numpy as np
from sentence_transformers import SentenceTransformer

model_name = 'all-MiniLM-L6-v2'
model = SentenceTransformer(model_name)

DOC_PATH = 'data/'
EMBEDDING_PATH = 'embeddings/'

documents = []

for file in os.listdir(DOC_PATH):
    file_path = os.path.join(DOC_PATH, file)

     # Make sure it's a file (not a folder)
    if os.path.isfile(file_path) and file.endswith('.txt'):
        with open(file_path, 'r', encoding='utf-8') as f:
            text = f.read()
            documents.append(text)
# Create embeddings for the documents
doc_embeddings = model.encode(documents)

# Create embeddings folder if it doesn't exist
os.makedirs(EMBEDDING_PATH, exist_ok=True)

# Save inside embeddings folder
np.save(os.path.join(EMBEDDING_PATH, 'doc_embeddings.npy'), doc_embeddings)
np.save(os.path.join(EMBEDDING_PATH, 'documents.npy'), documents)

print("Knowledge base embedded successfully ✅")
print(f"Total documents: {len(documents)}")
print(f"Embedding shape: {doc_embeddings.shape}")