from dotenv import load_dotenv
import os
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

load_dotenv()

def chunk_code_files(code_files):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=100
    )

    chunks = []

    for file in code_files:
        content = file["content"]

        split_chunks = splitter.split_text(content)

        for chunk in split_chunks:
            chunks.append({
                "file_path": file["file_path"],
                "content": chunk
            })

    return chunks


def create_vector_store(chunks):

    texts = []
    metadata = []

    for chunk in chunks:
        texts.append(chunk["content"])
        metadata.append({"file_path": chunk["file_path"]})

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vector_store = FAISS.from_texts(
        texts,
        embeddings,
        metadatas=metadata
    )

    return vector_store