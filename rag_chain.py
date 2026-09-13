from langchain_core.runnables import RunnablePassthrough

from rag_prompt import RAG_PROMPT


def create_rag_chain(retriever, llm):
    """Create the reusable EduBot RAG chain."""
    return (
        {
            "context": retriever,
            "question": RunnablePassthrough()
        }
        | RAG_PROMPT
        | llm
    )
