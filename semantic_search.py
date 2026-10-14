from ollama import Client
import math

client = Client(host="http://127.0.0.1:11434")

documents = [
    "Python is a programming language used to build software.",
    "Artificial intelligence helps computers perform intelligent tasks.",
    "Cars need regular maintenance and engine repairs.",
]

# Convert documents into vectors
result = client.embed(model="all-minilm", input=documents)

document_vectors = result.embeddings


def cosine_similarity(a, b):
    dot = sum(x * y for x, y in zip(a, b))

    magnitude_a = math.sqrt(sum(x * x for x in a))
    magnitude_b = math.sqrt(sum(y * y for y in b))

    if magnitude_a == 0 or magnitude_b == 0:
        return 0.0

    return dot / (magnitude_a * magnitude_b)


# Ask a question
query = input("Ask a question: ")

# Convert the question into a vector
query_result = client.embed(model="all-minilm", input=query)

query_vector = query_result.embeddings[0]

# Compare the question with every document
scores = []

for document, vector in zip(documents, document_vectors):
    score = cosine_similarity(query_vector, vector)
    scores.append((score, document))

# Show the best match first
scores.sort(reverse=True, key=lambda item: item[0])

print("\nBest matching documents:")

for score, document in scores:
    print(f"\nSimilarity: {score:.3f}")
    print(document)
