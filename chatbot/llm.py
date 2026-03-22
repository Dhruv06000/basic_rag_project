from google import genai
from google.genai import types
from .utils import clean_response
from config import GEMINI_API_KEY, LLM_MODEL, MAX_TOKENS, TEMPERATURE, TOP_P

client = genai.Client(api_key=GEMINI_API_KEY)


def generate_response(messages, temperature=None, top_p=None, **kwargs):

    prompt = "\n".join([f"{m['role']}: {m['content']}" for m in messages])

    try:
        response = client.models.generate_content(
            model=LLM_MODEL,
            contents=prompt,
            config=types.GenerateContentConfig(
                temperature=temperature if temperature is not None else TEMPERATURE,
                top_p=top_p if top_p is not None else TOP_P,
                max_output_tokens=MAX_TOKENS
            )
        )

        content = clean_response(response.text)

        return {
            "role": "assistant",
            "content": content
        }

    except Exception as e:
        print("ERROR:", e)
        return {
            "role": "assistant",
            "content": "⚠️ Something went wrong while generating a response."
        }