# test_rag.py
from rag_app import ask_question

query = "What is the company's policy on remote work?"
answer, sources = ask_question(query)

print("Answer:", answer)
print("\nSources Used:")
for i, src in enumerate(sources):
    print(f"[{i+1}] {src.metadata['source']}")
