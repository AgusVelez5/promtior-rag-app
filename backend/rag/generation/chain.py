from langchain_openai import ChatOpenAI
from langchain.chains.combine_documents import create_stuff_documents_chain
from .prompt import RAG_PROMPT

def build_generation_chain():
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
    return create_stuff_documents_chain(llm, RAG_PROMPT)