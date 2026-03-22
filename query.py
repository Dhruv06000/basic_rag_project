from src.embed import embed_query
from src.retrieve import retrieve
from config import RETRIEVAL_TOP_K
from chatbot.llm import generate_response

while True:

    query = input("\nAsk a question (or type 'exit'): ")

    if query.lower() == "exit":
        break

    # Step 1: Embed query
    query_embedding = embed_query(query)

    # Step 2: Retrieve relevant chunks
    results = retrieve(query_embedding, RETRIEVAL_TOP_K, with_scores=True)

    print("\nTop Retrieved Chunks:\n")

    context_list = []

    # ✅ FIX: results contains only chunks (no score)
    for i, (chunk, score) in enumerate(results):
        print(f"Result {i+1} (score={score:.3f}):\n{chunk[:200]}...\n")
        context_list.append(f"Document {i+1}:\n{chunk}")

    # Step 3: Build context
    context = "\n\n".join(context_list)

    # Step 4: Create messages (chatbot format)
    messages = [
        {
            "role": "system",
            "content": (
                    "You are a helpful AI assistant. "
                    "Answer using the provided context, but explain in your own words. "
                    "Keep the answer clear and concise. "
                    "If the answer is not in the context, say 'I don't know'. "
                    "Also mention which document number the answer came from."
     )
        },
        {
            "role": "user",
            "content": f"Context:\n{context}\n\nQuestion:\n{query}"
        }
    ]

    # Step 5: Generate response using Gemini
    response = generate_response(messages)

    print("\nFinal Response:\n")
    print(response["content"])