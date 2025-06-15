# openai_client.py

from dotenv import load_dotenv
import os
from openai import OpenAI

# 1. Load .env (so environment variables are available)
load_dotenv()

# 2. Read the key
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise RuntimeError("OPENAI_API_KEY not found in environment or .env file")

# 3. Instantiate the client with the key
client = OpenAI(api_key=api_key)

# 4. Default model
MODEL = os.getenv("OPENAI_MODEL", "gpt-4o")

# 5. Helper
def chat_completion(messages, **kwargs):
    return client.chat.completions.create(
        model=MODEL,
        messages=messages,
        **kwargs
    )
