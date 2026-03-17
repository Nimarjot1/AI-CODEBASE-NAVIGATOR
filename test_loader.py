from repo_loader import clone_repo, load_code_files
from embedder import chunk_code_files, create_vector_store
from rag_engine import create_rag_chain


# ---------------------------
# STEP 1: Load Repo
# ---------------------------
repo = clone_repo("https://github.com/expressjs/express")

files = load_code_files(repo)

print("Number of code files:", len(files))


# ---------------------------
# STEP 2: Chunk Code
# ---------------------------
chunks = chunk_code_files(files)

print("Number of chunks:", len(chunks))


# ---------------------------
# STEP 3: Create Vector Store
# ---------------------------
vector_store = create_vector_store(chunks)

print("Vector store created successfully")


# ---------------------------
# STEP 4: Create RAG Engine
# ---------------------------
qa = create_rag_chain(vector_store)


# ---------------------------
# STEP 5: Ask Questions (Loop 🔥)
# ---------------------------
while True:
    question = input("\nAsk a question (or type 'exit'): ")

    if question.lower() == "exit":
        break

    answer = qa(question)

    print("\nAI Answer:\n")
    print(answer)