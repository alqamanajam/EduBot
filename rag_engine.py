"""
EduBot - Person 1: RAG & Knowledge Engine

Responsibilities:
- PDF loading
- Text cleaning
- Chunking
- Hugging Face embeddings
- Chroma vector store
- Semantic retrieval
- Source/page metadata

PRD LLM:
Google Gemini 1.5 Flash

Embedding model:
sentence-transformers/all-MiniLM-L6-v2
"""

import os

import chromadb
from langchain_community.document_loaders import PyPDFLoader
from langchain_core.documents import Document
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter


EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
COLLECTION_NAME = "edubot_knowledge"
DEFAULT_CHUNK_SIZE = 1000
DEFAULT_CHUNK_OVERLAP = 200
DEFAULT_TOP_K = 4


def clean_document_text(documents):
    """Remove invalid Unicode surrogate characters safely."""
    clean_documents = []

    for doc in documents:
        clean_text = doc.page_content.encode(
            "utf-8",
            errors="replace"
        ).decode("utf-8")

        clean_documents.append(
            Document(
                page_content=clean_text,
                metadata=dict(doc.metadata)
            )
        )

    return clean_documents


def load_pdf(pdf_path):
    """Load a PDF using PyPDFLoader and clean its text."""
    if not os.path.exists(pdf_path):
        raise FileNotFoundError(f"PDF not found: {pdf_path}")

    documents = PyPDFLoader(pdf_path).load()
    return clean_document_text(documents)


def split_documents(
    documents,
    chunk_size=DEFAULT_CHUNK_SIZE,
    chunk_overlap=DEFAULT_CHUNK_OVERLAP
):
    """Split documents into overlapping chunks."""
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )

    return splitter.split_documents(documents)


def create_embeddings():
    """Create the PRD-compatible local Hugging Face embedding model."""
    return HuggingFaceEmbeddings(
        model_name=EMBEDDING_MODEL
    )


def create_vectorstore(embeddings):
    """
    Create an in-memory Chroma vector store.

    EphemeralClient is used because persistent Chroma produced a
    read-only SQLite issue during the Colab development setup.
    """
    client = chromadb.EphemeralClient()

    return Chroma(
        client=client,
        collection_name=COLLECTION_NAME,
        embedding_function=embeddings
    )


def build_knowledge_base(pdf_path):
    """Build the complete PDF -> chunks -> Chroma knowledge base."""
    documents = load_pdf(pdf_path)
    chunks = split_documents(documents)

    embeddings = create_embeddings()
    vectorstore = create_vectorstore(embeddings)

    batch_size = 100

    for start in range(0, len(chunks), batch_size):
        vectorstore.add_documents(
            chunks[start:start + batch_size]
        )

    return vectorstore, chunks


def get_retriever(vectorstore, top_k=DEFAULT_TOP_K):
    """Create a LangChain semantic retriever."""
    return vectorstore.as_retriever(
        search_kwargs={"k": top_k}
    )


def retrieve_documents(vectorstore, question, top_k=DEFAULT_TOP_K):
    """Retrieve the most relevant chunks for a question."""
    return vectorstore.similarity_search(
        question,
        k=top_k
    )


def format_context(documents):
    """Format retrieved chunks for the Gemini RAG prompt."""
    context_parts = []

    for doc in documents:
        page = doc.metadata.get("page")

        if page is not None:
            source_label = f"[Source: Page {page + 1}]"
        else:
            source_label = "[Source: Unknown]"

        context_parts.append(
            f"{source_label}\n{doc.page_content}"
        )

    return "\n\n".join(context_parts)


def get_sources(documents):
    """Return unique source/page references for the UI."""
    sources = []
    seen = set()

    for doc in documents:
        page = doc.metadata.get("page")
        source = doc.metadata.get(
            "source",
            "Uploaded document"
        )

        key = (source, page)

        if key in seen:
            continue

        seen.add(key)

        sources.append({
            "source": os.path.basename(source),
            "page": page + 1 if page is not None else None
        })

    return sources
