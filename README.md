# 🚀 AI Codebase Navigator

### 🔍 Semantic Search + RAG for GitHub Repositories

AI Codebase Navigator is an AI-powered system that enables developers to **understand and explore large codebases using natural language queries** instead of traditional keyword search.

It combines **vector search + Retrieval-Augmented Generation (RAG)** to locate and explain relevant parts of a repository.

---

# 💡 Problem

Modern repositories contain **thousands of files and millions of lines of code**.

Developers often struggle with questions like:

* Where is middleware implemented?
* How does routing work?
* Which files handle authentication?
* Where is a specific feature defined?

Traditional tools like `grep` or GitHub search rely on **exact keyword matching**, which often fails.

LLMs can help — but:

❌ They cannot read entire repositories
❌ Context window is limited

👉 So we need a system that retrieves only **relevant code** before asking the model.

---

# 🎯 Solution

This project implements a **Retrieval-Augmented Generation (RAG) pipeline for codebases**:

```
GitHub Repo
   ↓
Code Loader
   ↓
Chunking
   ↓
Embeddings (MiniLM)
   ↓
Vector Database (FAISS)
   ↓
Retriever
   ↓
Local LLM (LLaMA3 via Ollama)
   ↓
Answer Generation
```

---

# ⚙️ Features

✅ Clone and process any GitHub repository
✅ Intelligent code chunking
✅ Semantic embeddings using transformers
✅ Vector search using FAISS
✅ Local LLM integration (Ollama — no API cost)
✅ Natural language query interface
✅ Debug view showing retrieved files

---

# 🧠 How It Works

### 1. Repository Ingestion

```python
repo = clone_repo("https://github.com/expressjs/express")
files = load_code_files(repo)
```

---

### 2. Code Chunking

* Splits large files into meaningful chunks
* Improves retrieval accuracy

```
Chunks created: 862
```

---

### 3. Embedding Generation

Model used:

```
sentence-transformers/all-MiniLM-L6-v2
```

Converts code → vectors for semantic understanding.

---

### 4. Vector Search

FAISS is used to retrieve the most relevant code:

```
Query → "What does app.use() do?"
```

---

### 5. RAG + LLM (🔥 Key Feature)

Retrieved code is passed to a **local LLM (LLaMA3 via Ollama)**:

```python
llm = ChatOllama(model="llama3")
```

This enables:

✔ Code explanation
✔ Context-aware answers
✔ Natural language interaction

---

# 🖥️ Example Output

```
🔍 Retrieved Files:
- repos/express/lib/application.js
- repos/express/lib/response.js

AI Answer:

'app.use()' is used to register middleware functions...
```

---

# 📁 Project Structure

```
backend/
│
├── repo_loader.py      # Clone + load repo files
├── embedder.py         # Chunking + embeddings + FAISS
├── rag_engine.py       # RAG pipeline + LLM
├── test_loader.py      # CLI interface
├── requirements.txt
```

---

# ⚡ Installation

```bash
git clone https://github.com/Nimarjot1/AI-CODEBASE-NAVIGATOR.git
cd AI-CODEBASE-NAVIGATOR/backend

pip install -r requirements.txt
```

---

# ▶️ Run the Project

```bash
python test_loader.py
```

Then ask:

```
What does app.use() do in Express?
```

---

# 🧪 Sample Output

✔ Repository loaded
✔ Chunks created
✔ Vector store built
✔ Relevant files retrieved
✔ AI-generated explanation

---

# 🧩 Tech Stack

* Python
* LangChain
* FAISS (Vector DB)
* Sentence Transformers
* Ollama (Local LLM - LLaMA3)
* GitPython

---

# 🔥 What Makes This Project Strong

This is NOT just a chatbot.

It demonstrates:

✔ RAG architecture
✔ Vector databases
✔ LLM integration
✔ Real-world developer tooling
✔ Scalable system design

👉 This is the same architecture used in:

* GitHub Copilot Workspace
* Sourcegraph Cody
* Cursor IDE

---

# 🚀 Future Improvements

* 🌐 Web UI (React + Node)
* 📊 Multi-repo indexing
* 🧠 Better ranking (rerankers)
* ⚡ Streaming responses
* 🔎 AST-based chunking (code-aware)

---

# 👩‍💻 Author

**Nimarjot Kaur**

🔗 GitHub:
https://github.com/Nimarjot1

🔗 LinkedIn:
https://www.linkedin.com/in/nimarjot-kaur-03039b273/

---

# ⭐ If you like this project

Give it a ⭐ on GitHub and share it!
