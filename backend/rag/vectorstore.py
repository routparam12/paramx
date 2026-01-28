# from langchain_openai import OpenAIEmbeddings
# from langchain_community.vectorstores import FAISS
# from .loader import load_documents

# def build_vectorstore():
#     documents = load_documents()
#     embeddings = OpenAIEmbeddings()
#     vectorstore = FAISS.from_documents(documents, embeddings)
#     return vectorstore


from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from .loader import load_documents

def build_vectorstore():
    documents = load_documents()

    embeddings = HuggingFaceEmbeddings(
        model_name="all-MiniLM-L6-v2"
    )

    vectorstore = FAISS.from_documents(documents, embeddings)
    return vectorstore

