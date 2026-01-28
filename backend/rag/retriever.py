from .vectorstore import build_or_load_vectorstore

_vectorstore = None


def get_vectorstore():
    global _vectorstore
    if _vectorstore is None:
        _vectorstore = build_or_load_vectorstore()
    return _vectorstore


def retrieve_documents(query: str, k: int = 3):
    vectorstore = get_vectorstore()
    retriever = vectorstore.as_retriever(search_kwargs={"k": k})
    return retriever.invoke(query)


def build_context(docs) -> str:
    """
    Converts retrieved documents into a clean text context.
    """
    return "\n\n".join(doc.page_content for doc in docs)
