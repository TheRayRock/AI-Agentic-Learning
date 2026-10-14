messages = []

# Save your first question
messages.append({"role": "user", "content": "My name is Shahnawaz."})

# Save the AI's answer
messages.append({"role": "assistant", "content": "Nice to meet you, Shahnawaz!"})

# Save your next question
messages.append({"role": "user", "content": "What is my name?"})

print(messages)
