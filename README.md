# LangChain Interview Practice

This repo is my practice for AI and LangChain interviews. It covers RAG, LangChain, LangGraph, agents and evaluation.

## Questions I am going to solve

The full list of 56 tasks is in [questions/QUESTIONS.md](questions/QUESTIONS.md), in the order I plan to solve them.

| Priority | Tasks | Focus |
| --- | --- | --- |
| Priority 1 | 28 | RAG pipeline, embeddings, LCEL chains, LangGraph, agents and retrieval metrics |
| Priority 2 | 11 | Python and SQL basics, debugging, hybrid search, reranking and testing |
| Priority 3 | 17 | ChromaDB operations, advanced retrieval, evaluation and safety checks |

## What you need

| Requirement | Used for | Where to get it |
| --- | --- | --- |
| Python 3.12 | Running the code | [python.org](https://www.python.org/downloads/) |
| ChromaDB | Vector database for storing and searching documents | Installed with `requirements.txt`, no separate server needed |
| HuggingFace embeddings | Turning text into vectors for ChromaDB | Installed with `requirements.txt`, and the model downloads the first time it runs |
| Groq API key | LLM that generates the answers | [console.groq.com/keys](https://console.groq.com/keys) |
| LangSmith API key | Tracing and debugging LLM runs | [smith.langchain.com](https://smith.langchain.com) |

Later tasks, such as LangGraph and FastAPI, need extra packages that aren't in `requirements.txt` yet.

## Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/sanskratipatel/Langchain-Interivew-Practice.git
   cd Langchain-Interivew-Practice
   ```

2. Create and activate a virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

   On Windows, run `python -m venv venv`, then `venv\Scripts\activate`.

3. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

   This is a large install, about 6 GB, because it includes PyTorch.

4. Create a `.env` file in the project root and add your keys:

   ```
   GROQ_API_KEY=your_groq_api_key
   LANGCHAIN_API_KEY=your_langsmith_api_key
   LANGCHAIN_TRACING_V2=true
   LANGCHAIN_PROJECT=langchain-interview-practice
   ```

   `.env` is listed in `.gitignore`, so your keys won't be committed.

5. Load the keys at the top of any script that uses them:

   ```python
   from dotenv import load_dotenv

   load_dotenv()
   ```

6. Set up ChromaDB. It runs inside your Python script, so you only need an embedding model and a folder for the data:

   ```python
   from langchain_chroma import Chroma
   from langchain_huggingface import HuggingFaceEmbeddings

   embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

   vector_store = Chroma(
       collection_name="practice",
       embedding_function=embeddings,
       persist_directory="chroma_db",
   )
   ```

   The `chroma_db/` folder is created automatically and is listed in `.gitignore`.

## Running the code

Run scripts from the project root:

```bash
python 01_load_pdf.py
python 02_load_multiple_pdfs.py
```
