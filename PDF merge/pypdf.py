from pypdf import PdfWriter
import os

folder = "."  # Set this to your PDF files directory
merger=PdfWriter()
files=[f for f in os.listdir(folder) if f.endswith(".pdf")]

for pdf in files:
    merger.append(pdf)

merger.write("Mergedpdf.pdf")
merger.close()
