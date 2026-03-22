import os
from dotenv import load_dotenv

load_dotenv()

# API Key
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if GEMINI_API_KEY is None:
    raise ValueError("GEMINI_API_KEY not found. Please add it to your .env file.")


# 🤖 LLM CONFIG (Gemini)

LLM_MODEL = "gemini-2.5-flash"

MAX_TOKENS = 500
TEMPERATURE = 0.5
TOP_P = 0.1
TOP_K = 0.7
REPETITION_PENALTY = None


# 🧠 EMBEDDING CONFIG

EMBEDDING_MODEL = "all-MiniLM-L6-v2"


# 📂 DATA PATHS

DOC_PATH = "data/raw"
PROCESSED_PATH = "data/processed/"

CHUNK_SIZE = 250
OVERLAP = 0.1

RETRIEVAL_TOP_K = 3

CHUNKS_FILE = "all_chunks.pkl"
EMBEDDINGS_FILE = "chunk_embeddings.npy"

