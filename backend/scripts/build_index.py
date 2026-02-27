import argparse

from rag.ingestion.loaders import load_pdf, load_web
from rag.ingestion.chunking import split_documents
from rag.ingestion.indexer import build_vectorstore

def main(pdf_path: str, url: str):
    docs = []

    if pdf_path:
        docs.extend(load_pdf(pdf_path))

    if url:
        docs.extend(load_web(url))

    chunks = split_documents(docs)
    build_vectorstore(chunks)

    print("Index built")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--pdf", type=str, default=None)
    parser.add_argument("--url", type=str, default=None)
    args = parser.parse_args()

    main(args.pdf, args.url)