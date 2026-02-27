from typing import List

from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser

MULTI_QUERY_TEMPLATE = """
You are an AI assistant.

Generate 5 different search queries that could help retrieve relevant
documents for the user's question.

Return one query per line.

Original question:
{question}
"""

_prompt = ChatPromptTemplate.from_template(MULTI_QUERY_TEMPLATE)

_llm = ChatOpenAI(temperature=0)

_parser = StrOutputParser()


def generate_multi_queries(question: str) -> List[str]:
    """Generate multiple search queries from a single question."""
    chain = _prompt | _llm | _parser
    output = chain.invoke({"question": question})
    queries = [
        q.strip()
        for q in output.split("\n")
        if q.strip()
    ]

    if question not in queries:
        queries.append(question)

    return queries