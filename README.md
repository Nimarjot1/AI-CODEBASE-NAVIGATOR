# AI Codebase Navigator
### Semantic Search Engine for Software Repositories

AI Codebase Navigator is an experimental system designed to **analyze and navigate large software repositories using semantic understanding instead of simple keyword search**.

Traditional search tools rely on exact keyword matching, which often fails when developers do not know the exact function names or identifiers.

This project explores how **embeddings and vector search** can enable developers to locate relevant code snippets across repositories using **semantic similarity**.

The system is being built as a **Retrieval-Augmented Generation (RAG) pipeline for codebases**, where the first goal is to build a reliable **code ingestion and indexing infrastructure**.

---

# The Problem

Modern software repositories contain **thousands of files and millions of lines of code**.

Developers often struggle with questions like:

- Where is authentication implemented?
- Which files handle middleware logic?
- Where is a particular feature defined?
- Which functions manipulate a certain data structure?

Traditional tools like `grep` or GitHub search depend on **exact keyword matching**, which is often insufficient.

Large Language Models (LLMs) could help answer these questions — but they **cannot read entire repositories due to context window limits**.

Therefore we need an intermediate system that:

1. Reads the repository
2. Breaks code into meaningful chunks
3. Converts those chunks into embeddings
4. Stores embeddings in a vector database
5. Retrieves relevant code when needed

This project focuses on building that **core infrastructure**.

---

# Project Goal

The goal of this project is to build an **AI-powered navigation layer for software repositories** that allows developers to explore large codebases using **semantic search and natural language queries**.

The system is being built incrementally using a **modular architecture**.

Current implementation focuses on:

- Repository ingestion  
- Code parsing  
- Code chunk generation  
- Embedding generation  
- Vector indexing  

Future versions will integrate **LLM reasoning for intelligent code understanding**.

---

# System Architecture

## Current Pipeline

```
GitHub Repository
        ↓
Repository Cloning
        ↓
Source Code Loader
        ↓
Code Chunking
        ↓
Embedding Generation
        ↓
Vector Database Index
```

## Future Architecture

```
GitHub Repo
   ↓
Chunking
   ↓
Embeddings
   ↓
Vector DB
   ↓
Retriever
   ↓
LLM Reasoning
   ↓
Answer Generation
```

---

# Current Implementation

The current version successfully performs **repository ingestion and semantic indexing**.

## Repository Loader

Clones a GitHub repository and loads source files.

Example:

```python
repo = clone_repo("https://github.com/expressjs/express")
files = load_code_files(repo)
```

Example output:

```
Number of code files: 141
```

---

## Code Chunking

Large files are divided into smaller logical segments so embeddings capture meaningful context.

Example output:

```
Number of chunks: 863
```

Chunking improves:

- Embedding quality
- Retrieval accuracy
- Vector indexing performance

---

## Embedding Generation

Each chunk is converted into a semantic vector representation using a transformer model.

Model used:

```
sentence-transformers/all-MiniLM-L6-v2
```

This allows the system to understand the **semantic meaning of code snippets**.

---

## Vector Indexing

Embeddings are stored in a vector database which enables fast similarity search.

Example capability:

```
Query: "Where is middleware implemented?"
```

The system retrieves the **most relevant code chunks** from the repository.

---

# Repository Structure

```
AI-CODEBASE-NAVIGATOR
│
├ repo_loader.py
├ embedder.py
├ main.py
├ test_loader.py
├ requirements.txt
```

### File Descriptions

- **repo_loader.py** → Clones and loads Git repositories  
- **embedder.py** → Handles chunking and embedding generation  
- **main.py** → Pipeline orchestration  
- **test_loader.py** → Debugging and ingestion testing  

---

# Installation

Clone the repository:

```
git clone https://github.com/Nimarjot1/AI-CODEBASE-NAVIGATOR.git
cd AI-CODEBASE-NAVIGATOR
```

Install dependencies:

```
pip install -r requirements.txt
```

---

# Running the Project

Run the ingestion pipeline:

```
python test_loader.py
```

Example output:

```
Number of code files: 141
Number of chunks: 863
Vector store created successfully
```

---

# Project Screenshot

Example of the system processing a GitHub repository and generating vector embeddings.



---

# Why This Project Exists

Most "AI code assistants" rely heavily on external APIs.

This project focuses on building the **core architecture of an AI code understanding system from scratch**, including:

- Repository ingestion
- Semantic indexing
- Retrieval pipelines
- Modular system design

Understanding these systems is important for building real-world **AI developer tools**.

---

# Future Improvements

Planned extensions include:

### Semantic Query Interface

Allow developers to ask questions like:

```
Where is request validation implemented?
```

---

### LLM Integration

Use retrieved code chunks as context for a language model to generate explanations.

---

### Web Interface

Build a frontend interface where developers can explore repositories interactively.

---

### Multi-Repository Indexing

Allow indexing of multiple repositories into one searchable knowledge base.

---

# Technologies Used

- Python
- SentenceTransformers
- Vector Database
- LangChain
- Git Repository APIs

---

# Author

**Nimarjot Kaur**  

GitHub  
https://github.com/Nimarjot1  

LinkedIn  
https://www.linkedin.com/in/nimarjot-kaur-03039b273/
