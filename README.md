# Promtior — RAG Chatbot

This project implements an end-to-end Retrieval-Augmented Generation (RAG) chatbot capable of answering questions based on a PDF document and a web source.

## Backend setup
```
cd backend

python -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt
```

Create .env with:

```
OPENAI_API_KEY=your_key_here
VECTORSTORE_DIR=data/vectorstore
```

Build vector store (local)
```
python scripts/build_index.py
```

Run API locally
```
uvicorn app.main:app --reload
curl http://localhost:8000/health
```
## Frontend setup
```
cd frontend
npm install
npm run dev
```

## Docker

```
docker compose up --build
```