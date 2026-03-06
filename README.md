# Simple RAG System (From Scratch)

A simple **Retrieval-Augmented Generation (RAG)** pipeline implemented in Python.
This project demonstrates the core components of a RAG system including document loading, chunking, embedding generation, semantic retrieval, and query processing.
The goal of this project is to understand how modern AI systems **retrieve relevant knowledge before generating responses**.

## Project Overview

This project implements a basic **RAG workflow** in two stages.

### 1️⃣ Indexing Pipeline (`index.py`)

The indexing pipeline prepares the data for retrieval.

Steps:

1. Load documents from dataset
2. Split documents into overlapping chunks
3. Save processed chunks
4. Generate vector embeddings for chunks
5. Store embeddings locally

This step is run **only once** (or when the dataset changes).

### 2️⃣ Query Pipeline (`query.py`)

The query pipeline performs semantic search on the indexed data.

Steps:

1. Accept a user query
2. Convert query into an embedding
3. Compare with stored embeddings
4. Retrieve the most relevant chunks using cosine similarity
5. Display the top results

## Project Structure

```
simple_rag/
│
├── data/
│ ├── processed/
│ │      ├──all_chunks.pkl
│ │      └──chunk_embeddings.npy
│ └── raw/
│      ├──doc1.txt
│      ├──doc2.txt
│      └──docn.txt
├── src/
│   ├── load_data.py
│   ├── chunk.py
│   ├── embed.py
│   ├── retrieve.py
│   └── generate.py
│
├── index.py
├── query.py
├── config.py
├── requirements.txt
└── README.md
```

## Components

1️⃣ Data Loading

load_data.py loads .txt documents from the dataset directory.

2️⃣ Chunking

chunk.py splits documents into fixed-size overlapping chunks.

Chunking helps preserve context during retrieval.

Example configuration:

- CHUNK_SIZE = 250
- OVERLAP = 0.1

3️⃣ Embedding Generation

embed.py converts text chunks into vector embeddings using:

- all-MiniLM-L6-v2

Embeddings are stored locally as:

- data/processed/chunk_embeddings.npy

4️⃣ Retrieval

retrieve.py performs semantic search using cosine similarity.

Steps:

Embed user query

Compare with stored embeddings

Return top K relevant chunks

Example:

- TOP_K = 3

## Running the Project

### Step 1 — Build the Index

```bash
python index.py
```

This will load documents, create chunks, generate embeddings and save them.

### Step 2 — Start Querying

```bash
python query.py
```

Example:

```
Ask a question (or type 'exit'): What is machine learning?

Top Retrieved Chunks:

Result 1 (score=0.87):
Machine learning is a branch of artificial intelligence...
```

## Dependencies

- Python 3.10+
- sentence-transformers
- numpy
- scikit-learn

## Installation

```bash
git clone https://github.com/YOUR_USERNAME/simple_rag.git
cd simple_rag

python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

## Future Improvements

- Add a Vector Database (FAISS / Chroma / Weaviate)
- Implement Hybrid Search (BM25 + Semantic Search)
- Add Re-ranking models
- Integrate an LLM for answer generation
- Build a self-evaluating RAG pipeline

## Learning Goals

- Understand how RAG systems work internally
- Document chunking strategies
- Embedding generation
- Vector similarity search
- Information retrieval for LLMs

## License

This project is for **educational purposes**.
