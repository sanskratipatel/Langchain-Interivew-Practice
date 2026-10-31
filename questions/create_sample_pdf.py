
# STEP 1: Import required library

from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas


# STEP 2: Define PDF file path

pdf_path = "data/sample.pdf"


# STEP 3: Create PDF object

pdf = canvas.Canvas(pdf_path, pagesize=A4)


# STEP 4: Define starting position

x = 50
y = 800


# STEP 5: Add content to PDF

content = [
    "Introduction to Python",
    "",
    "Python is a high-level programming language.",
    "Python is used for backend development.",
    "Python is also used in Machine Learning.",
    "Python is widely used in Artificial Intelligence.",
    "",
    "Introduction to LangChain",
    "",
    "LangChain is a framework for building LLM applications.",
    "It provides document loaders and text splitters.",
    "It helps developers build RAG applications.",
    "",
    "Introduction to RAG",
    "",
    "RAG stands for Retrieval Augmented Generation.",
    "RAG retrieves relevant information from documents.",
    "The retrieved information is passed to an LLM."
]


# STEP 6: Write text into PDF

for line in content:

    pdf.drawString(x, y, line)

    y = y - 25


# STEP 7: Save PDF

pdf.save()


print("PDF created successfully!")
print("PDF Location:", pdf_path)


