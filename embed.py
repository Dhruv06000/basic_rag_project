import os
import numpy as np
from sentence_transformers import SentenceTransformer

model_name = 'all-MiniLM-L6-v2'
model = SentenceTransformer(model_name)

DOC_PATH = 'data/'

documents = []

for file in os.listdir(DOC_PATH):
    file_path = os.path.join(DOC_PATH, file)

     # Make sure it's a file (not a folder)
    if os.path.isfile(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            text = f.read()
            documents.append(text)
# Create embeddings for the documents
doc_embeddings = model.encode(documents)

#save the embeddings and documents for later use
np.save('doc_embeddings.npy', doc_embeddings)
np.save('documents.npy', documents)
print("Knowledge base embedded successfully ✅")