from src.embed import embed_query
from src.retrieve import retrieve
from config import TOP_K

while True:

    query = input("\nAsk a question (or type 'exit'): ")

    if query.lower() == "exit":
        break

    query_embedding = embed_query(query)

    results = retrieve(query_embedding, TOP_K)

    print("\nTop Retrieved Chunks:\n")

    for i, (chunk, score) in enumerate(results):
        print(f"Result {i+1} (score={score:.3f}):\n{chunk}\n")