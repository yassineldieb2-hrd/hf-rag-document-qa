from sentence_transformers import SentenceTransformer, util
from chunk import load_chunks

model = SentenceTransformer("all-MiniLM-L6-v2")
chunks = load_chunks()
chunk_embeddings = model.encode([c["text"] for c in chunks])


def search(question, top_k=3):
    q_emb = model.encode(question)
    scores = util.cos_sim(q_emb, chunk_embeddings)[0]
    top = scores.argsort(descending=True)[:top_k]
    return [(chunks[int(i)], float(scores[i])) for i in top]


if __name__ == "__main__":
    for chunk, score in search("How long does shipping take?"):
        print(f"\n{score:.2f} [{chunk['source']}] {chunk['text'][:80]}")