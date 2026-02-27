from langchain_community.document_loaders import (
    PyPDFLoader,
    WebBaseLoader,
)

def load_pdf(path: str):
    return PyPDFLoader(path).load()

def load_web(url: str):
    return WebBaseLoader(url).load()