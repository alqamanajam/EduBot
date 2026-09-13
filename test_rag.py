"""
Person 1 end-to-end RAG test.

Place the permitted PDF in this folder and set PDF_PATH below.

Required environment variable:
GOOGLE_API_KEY=your_key
"""

from rag_engine import (
    build_knowledge_base,
    get_retriever,
    get_sources,
)
from gemini_llm import create_llm
from rag_chain import create_rag_chain


PDF_PATH = "Python Data Science Handbook.pdf"


def main():
    print("Building knowledge base...")
    vectorstore, chunks = build_knowledge_base(PDF_PATH)

    print("Chunks created:", len(chunks))
    print("Knowledge base ready.")

    retriever = get_retriever(vectorstore, top_k=4)
    llm = create_llm()

    rag_chain = create_rag_chain(retriever, llm)

    question = "What is NumPy and why is it useful in data science?"

    print("\nQuestion:", question)
    response = rag_chain.invoke(question)

    print("\nAnswer:")
    print(response.content)

    docs = vectorstore.similarity_search(question, k=4)

    print("\nSources:")
    for source in get_sources(docs):
        print(source)


if __name__ == "__main__":
    main()
