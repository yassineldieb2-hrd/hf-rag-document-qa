import os
from huggingface_hub import InferenceClient
from search import search

client = InferenceClient(api_key=os.environ["HF_TOKEN"])


def ask(question):
    results = search(question, top_k=3)
    results = [(c, s) for c, s in results if s >= 0.3]
    if not results:
        return "I don't know based on the document.", []
    context = "\n\n".join(chunk["text"] for chunk, score in results)
    sources = sorted({chunk["source"] for chunk, score in results})

    prompt = f"""You answer questions using the context below.

Rules:
1. Find the sentence in the context that relates to the question.
2. You may compare numbers (for example, 19 days is more than 14 days).
3. Only say "I don't know based on the document." if nothing in the context relates to the question.

Context:
{context}

Question: {question}

Answer in 1 to 2 short sentences. Include every relevant option from the context, and do not make the decision for the customer."""

    response = client.chat_completion(
        model="meta-llama/Llama-3.1-8B-Instruct",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=200,
    )
    return response.choices[0].message.content, sources


if __name__ == "__main__":
    while True:
        question = input("\nAsk a question (or type 'quit'): ")
        if question.lower() == "quit":
            break
        answer, sources = ask(question)
        print("A:", answer)
        print("Sources:", ", ".join(sources))
