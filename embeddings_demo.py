from ollama import Client
import math

client = Client(host="http://127.0.0.1:11434")

sentences = [
    "I love learning artificial intelligence.",
    "I enjoy studying AI.",
    "i like to learn about AI",
]

# Convert each sentence into a vector
response = client.embed(model="all-minilm", input=sentences)

vectors = response.embeddings


def cosine_similarity(a, b):
    dot_product = sum(x * y for x, y in zip(a, b))

    magnitude_a = math.sqrt(sum(x * x for x in a))
    magnitude_b = math.sqrt(sum(y * y for y in b))

    if magnitude_a == 0 or magnitude_b == 0:
        return 0.0

    return dot_product / (magnitude_a * magnitude_b)


score1 = cosine_similarity(vectors[0], vectors[1])
score2 = cosine_similarity(vectors[0], vectors[2])

print("Similar meanings:")
print(round(score1, 3))

print("\nDifferent meanings:")
print(round(score2, 3))
