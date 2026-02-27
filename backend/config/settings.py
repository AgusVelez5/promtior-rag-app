import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
VECTORSTORE_DIR = os.getenv("VECTORSTORE_DIR", "data/vectorstore")
CHUNK_SIZE = 600
CHUNK_OVERLAP = 120
TOP_K = 8
MULTI_QUERY_ENABLED = True
MULTI_QUERY_COUNT = 5