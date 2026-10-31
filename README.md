# LangChain Interview Practice

Hands-on practice for AI and LangChain interviews. Each numbered script covers one concept, starting with loading documents, the first step of a RAG pipeline.

## What's covered so far

| Script | What it practises |
| --- | --- |
| `01_load_pdf.py` | Load one PDF with `PyPDFLoader` and inspect each document's text and metadata |
| `02_load_multiple_pdfs.py` | Find every PDF in a folder and combine them into one list of documents |

## Project structure

```
.
├── 01_load_pdf.py                  # Load a single PDF
├── 02_load_multiple_pdfs.py        # Load all PDFs in data/
├── data/
│   ├── sample.pdf                  # Python, LangChain and RAG notes
│   └── second.pdf                  # Machine Learning notes
├── questions/
│   ├── create_sample_pdf.py        # Generates data/sample.pdf
│   └── 2create_sample_pdf.py       # Generates data/second.pdf
├── requirements.txt
└── README.md
```

## Setup

This project is tested on Python 3.12.

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

   On Windows, activate it with `venv\Scripts\activate`.

3. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Running the scripts

Run everything from the project root, because the scripts use paths such as `data/sample.pdf`.

```bash
python 01_load_pdf.py
python 02_load_multiple_pdfs.py
```

The sample PDFs are already in `data/`. To regenerate them:

```bash
python questions/create_sample_pdf.py
python questions/2create_sample_pdf.py
```

## Environment variables (optional)

The current scripts don't need API keys, so you can skip this step for now. For LangSmith tracing in later exercises, create a `.env` file in the project root:

```
LANGCHAIN_API_KEY=your_api_key
LANGCHAIN_TRACING_V2=true
LANGCHAIN_PROJECT=your_project_name
```

`.env` is listed in `.gitignore`, so it won't be committed.

## Troubleshooting

| Error | Cause | Fix |
| --- | --- | --- |
| `pypdf.errors.EmptyFileError: Cannot read an empty file` | A file in `data/` is 0 bytes, for example one created with `touch` | Delete it or replace it with a real PDF |
| `FileNotFoundError: ... 'data/sample.pdf'` | The script was run from outside the project root | `cd` to the project root and run it again |
