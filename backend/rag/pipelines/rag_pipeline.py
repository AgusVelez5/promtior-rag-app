from langchain_core.runnables import RunnableLambda
from rag.ingestion.indexer import load_vectorstore
from rag.retrieval.retriever import MultiQueryRetriever
from rag.generation.chain import build_generation_chain


def build_rag_chain():
    vectorstore = load_vectorstore()
    retriever = MultiQueryRetriever(vectorstore)
    combine_docs_chain = build_generation_chain()

    def retrieve(inputs: dict):
        question = inputs["question"]
        docs = retriever.get_relevant_documents(question)
        return {"context": docs, "input": question}

    retrieval_runnable = RunnableLambda(retrieve)
    rag_chain = retrieval_runnable | combine_docs_chain
    return rag_chain