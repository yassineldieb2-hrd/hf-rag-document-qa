from sentence_transformers import SentenceTransformer
from chunk import load_chunks

model = SentenceTransformer("all-MiniLM-L6-v2")

chunks = load_chunks()
embeddings = model.encode(chunks)

print("Number of chunks:", len(chunks))
print("Embeddings shape:", embeddings.shape)
print("First 5 numbers of chunk 1:", embeddings[1][:5])