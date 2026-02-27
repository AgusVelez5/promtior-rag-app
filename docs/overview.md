# Promtior RAG App

## Overview

For this challenge, I implemented a RAG chatbot capable of answering questions grounded in a PDF document and a web source. From the outset, I knew nothing about these types of projects and their technologies, so I set about researching them to understand the objectives that these types of solutions seek to address, how they do so, and what technologies they use. I did this by reading different types of posts, watching videos, and discussing with ChatGPT mainly the architecture and best practices in RAG.

The solution follows the standard RAG pattern: documents are ingested, transformed into embeddings, stored in a vector database, and later retrieved at query time to augment the language model prompt. 

## Main Challenges and Solutions

### Challenge 1: Dependency and version conflicts
During setup, multiple incompatibilities appeared between LangChain, FastAPI, Pydantic, and supporting libraries.

Solution:

- Standardized package versions

- Recreated the virtual environment

- Locked dependencies in requirements.txt


### Challenge 2: Empty vector store in production

Initially, the ECS deployment returned generic answers because the vector store was empty. The root cause was that the container started without indexed data, so the retrieval function returned zero relevant chunks.

Solution:

- Added ingestion at container startup, due the lack of a pipeline.

### Challenge 3: Retrieval quality issues

Some factual questions (e.g., founding date) were not answered correctly during testing. The issue was traced to the ingestion layer. The PDF content was not being properly extracted (empty text chunks). As a result, the vector store was dominated by website content.

Solution

- Fixed PDF ingestion to ensure proper text extraction.

## Final Result

The final system is a fully working RAG chatbot that:

- Retrieves knowledge from PDF and web sources
- Generates grounded answers in Spanish
- Runs locally with Docker Compose
- Deploys to AWS using Terraform
- Exposes a production-ready API via LangServe
- Provides a simple React UI

The architecture is intentionally simple but follows production best practices (in general).