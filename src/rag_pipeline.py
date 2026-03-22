from src.retrieve import retrieve
from chatbot.llm import generate_response

def ask(query):

    # Step 1: Retrieve relevant docs
    retrieved_docs = retrieve(query)

    # Step 2: Build context
    context = "\n\n".join([
        f"Document {i+1}:\n{doc}"
        for i, doc in enumerate(retrieved_docs[:3])
    ])

    # Step 3: Create messages (your chatbot format)
    messages = [
        {
            "role": "system",
            "content": "You are a helpful AI assistant. Answer ONLY using the provided context."
        },
        {
            "role": "user",
            "content": f"Context:\n{context}\n\nQuestion:\n{query}"
        }
    ]

    # Step 4: Generate answer using Gemini
    response = generate_response(messages)

    return response["content"]