import os
from pypdf import PdfReader


def read_file(path):
    if path.lower().endswith(".pdf"):
        reader = PdfReader(path)
        return "\n".join(page.extract_text() or "" for page in reader.pages)
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def split_text(text, size=500, overlap=100):
    text = " ".join(text.split())
    pieces = []
    start = 0
    while start < len(text):
        pieces.append(text[start:start + size])
        start += size - overlap
    return pieces


def load_chunks(folder="docs"):
    chunks = []
    for name in os.listdir(folder):
        if not name.lower().endswith((".txt", ".pdf")):
            continue
        text = read_file(os.path.join(folder, name))
        for piece in split_text(text):
            chunks.append({"text": piece, "source": name})
    return chunks


if __name__ == "__main__":
    chunks = load_chunks()
    print(f"Total chunks: {len(chunks)}")
    for c in chunks[:3]:
        print(f"\n[{c['source']}] {c['text'][:100]}")