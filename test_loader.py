from repo_loader import clone_repo, load_code_files

repo = clone_repo("https://github.com/expressjs/express")

files = load_code_files(repo)

print("Number of code files:", len(files))

print("First file preview:\n")
print(files[0]["content"][:500])

from embedder import chunk_code_files

chunks = chunk_code_files(files)

print("Number of chunks:", len(chunks))
print("\nExample chunk:\n")
print(chunks[0]["content"])

from embedder import create_vector_store

vector_store = create_vector_store(chunks)

print("Vector store created successfully")

from rag_engine import create_rag_chain

qa = create_rag_chain(vector_store)

question = "Where is routing implemented in this repository?"

answer = qa(question)

print("\nAI Answer:\n")
print(answer)