from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings


def chunk_code_files(code_files):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=100
    )

    chunks = []

    for file in code_files:
        content = file["content"]
        file_path = file["file_path"]

        # 🔥 metadata tagging
        file_type = "normal"

        if "lib/router" in file_path:
            file_type = "router"
        elif "lib/application" in file_path:
            file_type = "application"
        elif "lib/" in file_path:
            file_type = "core"

        split_chunks = splitter.split_text(content)

        for chunk in split_chunks:
            chunks.append({
                "file_path": file_path,
                "content": chunk,
                "file_type": file_type
            })

    return chunks


def create_vector_store(chunks):

    texts = [chunk["content"] for chunk in chunks]

    metadata = [
        {
            "file_path": chunk["file_path"],
            "file_type": chunk["file_type"]
        }
        for chunk in chunks
    ]

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vector_store = FAISS.from_texts(
        texts,
        embeddings,
        metadatas=metadata
    )

    return vector_store
