PHASE 1 — Build a Basic RAG (Minimal but Clean)

Start SIMPLE. Don’t build hybrid yet.

Step 1 — Project Structure

rag_project/
│
├── data/                  # your 20 ML .txt files
├──embeddings/             # to store embedding of knowlage base
├── embed.py               # creates embeddings
├── retriever.py           # semantic search
├── rag.py                 # full pipeline
├── llm.py                 # Connect to an LLM
└── requirements.txt
