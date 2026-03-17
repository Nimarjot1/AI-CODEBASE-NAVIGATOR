from langchain_ollama import ChatOllama
import os


def create_rag_chain(vector_store):

    llm = ChatOllama(
        model="llama3",
        temperature=0
    )

    retriever = vector_store.as_retriever(search_kwargs={"k": 8})

    def ask(question):

        # ---------------------------
        # STEP 1: Normal retrieval
        # ---------------------------
        docs = retriever.invoke(question)

        # ---------------------------
        # STEP 2: FORCE LOAD ROUTER FILES 🔥
        # ---------------------------
        extra_docs = []

        for root, _, files in os.walk("repos/express/lib/router"):
            for file in files:
                if file.endswith(".js"):
                    path = os.path.join(root, file)

                    try:
                        with open(path, "r", encoding="utf-8") as f:
                            extra_docs.append(
                                type("Doc", (), {
                                    "page_content": f.read()[:800],
                                    "metadata": {"file_path": path}
                                })
                            )
                    except:
                        pass

        # merge retrieved + forced docs
        docs = docs + extra_docs

        # ---------------------------
        # STEP 3: REMOVE DUPLICATES
        # ---------------------------
        seen = set()
        unique_docs = []

        for d in docs:
            path = d.metadata.get("file_path", "")
            if path not in seen:
                seen.add(path)
                unique_docs.append(d)

        docs = unique_docs

        # ---------------------------
        # STEP 4: DEBUG
        # ---------------------------
        print("\n🔍 Retrieved Files:")
        for doc in docs:
            print("-", doc.metadata.get("file_path", "unknown"))

        # ---------------------------
        # STEP 5: BUILD CONTEXT
        # ---------------------------
        context_parts = []

        for i, doc in enumerate(docs):
            context_parts.append(
                f"""
[Chunk {i+1}]
File Path: {doc.metadata.get("file_path")}

Code:
{doc.page_content[:800]}
"""
            )

        context = "\n\n".join(context_parts)

        # ---------------------------
        # STEP 6: PROMPT
        # ---------------------------
        prompt = f"""
You are a senior software engineer analyzing a GitHub repository.

STRICT RULES:
- Answer ONLY using provided code
- Mention file paths EXACTLY as given
- Focus on router and application files
- Do NOT give generic explanations
- Do NOT invent anything

Code Context:
{context}

Question:
{question}

Answer:
"""

        response = llm.invoke(prompt)

        return response.content

    return ask