from openai_client import chat_completion

from openai_client import chat_completion

def main():
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user",   "content": "Say hello in one sentence."}
    ]
    resp = chat_completion(messages, temperature=0)
    print("Model response:", resp.choices[0].message.content)

if __name__ == "__main__":
    main()

print(resp.choices[0].message.content)
