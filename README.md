# Langchain.RAG-Conversational.Chatbot

Overview

LionO Chatbot is an AI-powered question-answering system that lets users interact with company data in natural language.
It uses Retrieval-Augmented Generation (RAG) to fetch information from multiple knowledge sources and generate precise answers.

Data sources include:

🌐 Web pages – company product & about-us pages

📄 PDFs – e.g., company history documents

📑 DOCX files – e.g., internal reports or notes

The chatbot runs on a Streamlit web UI, making it simple and interactive.

🎥 Preview

Here’s a quick look at the chatbot in action:

(Replace ./assets/screenshot.png with the path/URL to your actual screenshot. You can host it inside an assets/ folder in the repo.)

🚀 Features

Multi-source ingestion: PDFs, DOCX, and webpages

Chunked text processing: via RecursiveCharacterTextSplitter

Semantic search: with ChromaDB vector store

LLM responses: powered by Groq LLM through LangChain

Conversational memory: context-aware chat history

User-friendly chat UI: built with Streamlit

🛠️ Tech Stack

LangChain – orchestration framework

HuggingFace Sentence Transformers – embeddings

Chroma – vector database

Groq LLM – response generation

Streamlit – UI framework

