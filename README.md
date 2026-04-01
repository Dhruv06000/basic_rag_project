# 🧠 Simple RAG System (From Scratch)

A simple **Retrieval-Augmented Generation (RAG)** system implemented in Python.

This project demonstrates how modern AI systems **retrieve relevant information and use an LLM (Gemini) to generate answers** instead of relying only on pre-trained knowledge.

---

## 🚀 Project Overview

This project implements a complete **RAG workflow** with two main stages:

### 1️⃣ Indexing Pipeline (`index.py`)

The indexing pipeline prepares the data for retrieval.

Steps:

1. Load documents from dataset
2. Split documents into overlapping chunks
3. Save processed chunks
4. Generate vector embeddings for chunks
5. Store embeddings locally

👉 This step is run **only once** (or when data changes).

---

### 2️⃣ Query + Generation Pipeline (`query.py`)

The query pipeline performs **semantic search + LLM-based answer generation**.

Steps:

1. Accept a user query
2. Convert query into an embedding
3. Retrieve top-K relevant chunks using cosine similarity
4. Pass retrieved context to LLM (Gemini)
5. Generate a final answer based on context
6. Display answer with source references

---

## 🔄 RAG Pipeline

```
User Query
    ↓
Query Embedding
    ↓
Vector Search (Top-K chunks)
    ↓
Context Injection
    ↓
LLM (Gemini)
    ↓
Final Answer
```

---
```
## 📁 Project Structure

simple_rag/
│
├── data/
│ ├── processed/
│ │ ├──all_chunks.pkl
│ │ └──chunk_embeddings.npy
│ └── raw/
│ ├──doc1.txt
│ ├──doc2.txt
│ └──docn.txt
├── src/
│ ├── load_data.py
│ ├── chunk.py
│ ├── embed.py
│ ├── retrieve.py
│ └── generate.py
│
├── chatbot/ # LLM integration module
│ ├── llm.py # Gemini API interaction
│ ├── context.py # Conversation handling (optional)
│ └── utils.py

├── index.py
├── query.py
├── config.py
├── requirements.txt
└── README.md

---
```
## ⚙️ Components

### 1️⃣ Data Loading

- Loads `.txt` documents from dataset
- Implemented in `load_data.py`

---

### 2️⃣ Chunking

- Splits documents into smaller chunks
- Helps improve retrieval accuracy

Example config:

- `CHUNK_SIZE = 250`
- `OVERLAP = 0.1`

---

### 3️⃣ Embedding Generation

- Uses `sentence-transformers` model:
  - `all-MiniLM-L6-v2`
- Converts text into dense vectors
- Stored as:
  - `chunk_embeddings.npy`

---

### 4️⃣ Retrieval

- Uses cosine similarity
- Returns **Top-K relevant chunks**

Key features:

- Fast NumPy-based search
- Optional similarity scores
- Supports debugging of retrieval quality

---

### 5️⃣ LLM Generation (NEW 🚀)

- Integrated **Google Gemini API**
- Uses retrieved chunks as context
- Generates final answer

Prompt design ensures:

- Answers are based on context
- Source references are included
- Reduces hallucination

---

## ▶️ Running the Project

### Step 1 — Build the Index

```bash
- python index.py

### Step 2 — Run Query System

- python query.py

## Example
Ask a question: What is machine learning?

Top Retrieved Chunks:

Result 1 (score=0.37): ...
Result 2 (score=0.36): ...

Final Answer:
Machine learning is a branch of AI...
(Document 3)


## 🛠️ Installation

git clone https://github.com/Dhruv06000/basic_rag_project
cd basic_rag_project

python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt

## Create a .env file:
- GEMINI_API_KEY=your_api_key_here

## 📊 Features

- ✅ End-to-end RAG pipeline
- ✅ Semantic search using embeddings
- ✅ Context-aware answer generation
- ✅ Source attribution
- ✅ Modular design (easy to extend)

## ⚠️ Limitations

- Retrieval ranking is not always perfect
- Small dataset (limited knowledge base)
- No hybrid search yet
- No re-ranking or evaluation step

🚀 Future Improvements

-  Hybrid search (keyword + semantic)
-  Re-ranking models
-  Self-evaluating RAG system
-  Vector database (FAISS / Pinecone)
-  Web UI (Flask / React)

📌 License

This project is for educational purposes.
```
