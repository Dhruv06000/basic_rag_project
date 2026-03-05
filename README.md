# Simple RAG System

This is a **basic Retrieval-Augmented Generation (RAG) system** built in Python.  
It demonstrates the core workflow of RAG: loading a knowledge base, chunking text, embedding, retrieving, and generating responses.

---

## 📂 Folder Structure

simple_rag/
│
├── data/
│ ├── processed/
│ │      ├──all_chunks.pkl
│ │      └──chunk_embeddings.npy
│ └── documents.txt    
│
├── src/
│ ├── load_data.py
│ ├── chunk.py
│ ├── embed.py
│ ├── retrieve.py
│ └── generate.py
│
├── main.py
├── config.py
├── requirements.txt
└── README.md

---

## ⚙️ Project Overview

The project follows these steps:

1. **Load knowledge base**  
   All `.txt` files from the `data/` folder are read and stored as documents.

2. **Chunking**  
   Each document is split into smaller overlapping chunks using `chunk_text()` function.  
   Overlap ensures semantic continuity across chunks for better retrieval.

3. **Embedding** _(to be implemented next)_  
   Each chunk will be converted into vector embeddings using an embedding model (e.g., SentenceTransformers).

4. **Retrieval** _(to be implemented next)_  
   Given a user query, the system will retrieve top-k most relevant chunks using cosine similarity.

5. **Generation** _(to be implemented next)_  
   Retrieved chunks will be used as context to generate responses via an LLM.

---

## 📌 Features Implemented

- Folder-based knowledge base support (`data/`)
- Overlap chunking of text documents
- Clean, modular folder structure
- Configurable parameters via `config.py`

---

## 📌 Next Steps

1. Implement **embedding creation** (`src/embed.py`)
2. Implement **retrieval mechanism** (`src/retrieve.py`)
3. Implement **generation pipeline** (`src/generate.py`)
4. Connect all modules in `main.py` to form a working RAG system

---

## 🛠️ Dependencies

- Python 3.10+
- `sentence-transformers` (for embeddings)
- `numpy` (for vector operations)
- `scikit-learn` (for cosine similarity)

Install dependencies via:

```bash
pip install -r requirements.txt
```
