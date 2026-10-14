# from ollama import Client

# client = Client(host="http://127.0.0.1:11434")

# response = client.chat(
#     model="qwen3:4b",
#     messages=[{"role": "user", "content": "Explain Agentic AI in simple English."}],
# )

# print(response.message.content)


from ollama import Client

client = Client(host="http://127.0.0.1:11434")

messages = [
    {
        "role": "system",
        "content": (
            "You are a senior Python developer with 15 years "
            "of experience. Teach beginners using simple English "
            "and practical examples."
        ),
    }
]

while True:
    question = input("\nYou: ")

    if question.lower() == "exit":
        print("Goodbye!")
        break

    messages.append({"role": "user", "content": question})

    response = client.chat(model="qwen3:4b", messages=messages)

    answer = response.message.content
    print("\nAI:", answer)

    messages.append({"role": "assistant", "content": answer})
