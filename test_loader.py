from repo_loader import clone_repo, load_code_files
from embedder import chunk_code_files, create_vector_store
from rag_engine import create_rag_chain

repo = clone_repo("https://github.com/expressjs/express")

files = load_code_files(repo)

chunks = chunk_code_files(files)

print("Number of chunks:", len(chunks))

vector_store = create_vector_store(chunks)

print("Vector store created successfully")

qa = create_rag_chain(vector_store)

while True:
    question = input("\nAsk a question (or type 'exit'): ")

    if question.lower() == "exit":
        break

    answer = qa(question)

    print("\nAI Answer:\n")
    print(answer)
