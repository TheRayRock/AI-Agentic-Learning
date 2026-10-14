import json
from pathlib import Path
from ollama import Client

client = Client(host="http://127.0.0.1:11434")

HISTORY_FILE = Path("chat_history.json")

SYSTEM_MESSAGE = {
    "role": "system",
    "content": (
        "You are a senior Python developer. "
        "Explain concepts in simple English with examples."
    ),
}


def load_history():
    if HISTORY_FILE.exists():
        try:
            return json.loads(HISTORY_FILE.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            print("Could not read history. Starting a new chat.")

    return [SYSTEM_MESSAGE.copy()]


def save_history(messages):
    HISTORY_FILE.write_text(
        json.dumps(messages, indent=2, ensure_ascii=False), encoding="utf-8"
    )


messages = load_history()

# Make sure the system instructions are present.
if not messages or messages[0].get("role") != "system":
    messages.insert(0, SYSTEM_MESSAGE.copy())

print("Chatbot ready! Type 'exit' to quit.")
print("Type 'clear' to start a fresh conversation.")

while True:
    question = input("\nYou: ").strip()

    if question.lower() == "exit":
        break

    if question.lower() == "clear":
        messages = [SYSTEM_MESSAGE.copy()]
        save_history(messages)
        print("Conversation cleared!")
        continue

    if not question:
        continue

    messages.append({"role": "user", "content": question})

    try:
        response = client.chat(model="qwen3:4b", messages=messages)

        answer = response.message.content
        print("\nAI:", answer)

        messages.append({"role": "assistant", "content": answer})

        save_history(messages)

    except Exception as error:
        messages.pop()  # Remove the failed user message
        print("Error:", error)
