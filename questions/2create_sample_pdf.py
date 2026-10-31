
from reportlab.pdfgen import canvas

pdf = canvas.Canvas("data/second.pdf")

pdf.drawString(100, 750, "Introduction to Machine Learning")
pdf.drawString(100, 720, "Machine Learning is a part of Artificial Intelligence.")
pdf.drawString(100, 690, "It helps computers learn patterns from data.")
pdf.drawString(100, 660, "Python provides libraries like Scikit-learn.")

pdf.save()

print("Second PDF created successfully!")
