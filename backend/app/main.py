from fastapi import FastAPI
from langserve import add_routes
from fastapi.middleware.cors import CORSMiddleware
from rag.pipelines.rag_pipeline import build_rag_chain

app = FastAPI(title="Promtior RAG App")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

rag_chain = build_rag_chain()
add_routes(
    app,
    rag_chain,
    path="/rag",
)

@app.get("/health")
def health():
    return {"status": "ok"}