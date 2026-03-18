from langchain_ollama import ChatOllama


def create_rag_chain(vector_store):

    # Local LLM
    llm = ChatOllama(
        model="llama3",
        temperature=0
    )

    retriever = vector_store.as_retriever(search_kwargs={"k": 6})

    def ask(question):

        # ---------------------------
        # STEP 1: Retrieve docs
        # ---------------------------
        docs = retriever.invoke(question)

        print("\n🔍 Retrieved Files:")
        for doc in docs:
            print("-", doc.metadata.get("file_path", "unknown"))

        # ---------------------------
        # STEP 2: Build context
        # ---------------------------
        context = "\n\n".join([
            f"File: {doc.metadata.get('file_path')}\n{doc.page_content[:1000]}"
            for doc in docs
        ])

        # ---------------------------
        # STEP 3: Simple Prompt (NO STRICT RULES)
        # ---------------------------
        prompt = f"""
You are an AI assistant helping understand a GitHub repository.

Use the code below to answer the question.

If exact implementation is not visible, explain based on available code.

Code:
{context}

Question:
{question}

Answer clearly:
"""

        # ---------------------------
        # STEP 4: Generate answer
        # ---------------------------
        response = llm.invoke(prompt)

        return response.content

    return ask
