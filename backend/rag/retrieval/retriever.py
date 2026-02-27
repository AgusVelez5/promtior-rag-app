from typing import List, Set

from langchain.schema import Document

from config.settings import TOP_K
from .multi_query import generate_multi_queries


def _unique_docs(docs: List[Document]) -> List[Document]:
    """Remove duplicate documents."""
    seen: Set[str] = set()
    unique = []

    for doc in docs:
        key = doc.page_content[:200]

        if key not in seen:
            seen.add(key)
            unique.append(doc)

    return unique


class MultiQueryRetriever:
    def __init__(self, vectorstore):
        self.vectorstore = vectorstore

    def get_relevant_documents(self, question: str) -> List[Document]:
        queries = generate_multi_queries(question)

        all_docs: List[Document] = []

        for q in queries:
            docs = self.vectorstore.similarity_search(q, k=TOP_K)
            all_docs.extend(docs)

        return _unique_docs(all_docs)