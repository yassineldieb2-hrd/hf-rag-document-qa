from rag import ask

TESTS = [
    ("How long does standard shipping take?", "5 to 7", "document.txt"),
    ("How much does express shipping cost?", "15", "document.txt"),
    ("How long is the warranty on electronics?", "2", "document.txt"),
    ("Does the warranty cover water damage?", "not", "document.txt"),
    ("What are the support hours?", "9:00", "document.txt"),
    ("Can I return a used item after 20 days?", "14", "document.txt"),
    ("What is Yassin's job title?", "Store Manager", "YASSIN CV.pdf"),
    ("Do you ship to Germany?", "don't know", None),
    ("What is the capital of France?", "don't know", None),
]

passed = 0
for question, expected, source in TESTS:
    answer, sources = ask(question)
    ok_answer = expected.lower() in answer.lower()
    ok_source = (source in sources) if source else (sources == [])
    ok = ok_answer and ok_source
    passed += ok
    print(f"{'PASS' if ok else 'FAIL'} | {question}")
    if not ok:
        print(f"   answer: {answer}")
        print(f"   sources: {sources} (expected: {source})")

print(f"\nScore: {passed}/{len(TESTS)}")
