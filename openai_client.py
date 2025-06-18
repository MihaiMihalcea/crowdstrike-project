# openai_client.py

from dotenv import load_dotenv
import os
from openai import OpenAI

# Load environment vars and instantiate the OpenAI client.
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
    """
    Send a chat-completion request to OpenAI.

    :param messages: list of {"role":..., "content":...} dicts.
    :param kwargs: any other OpenAI parameters (temperature, etc.).
    """
    return client.chat.completions.create(
        model=MODEL,
        messages=messages,
        **kwargs
    )
