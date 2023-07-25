import PyPDF2

PdfFiles = ["module 7.pdf", "module 8.pdf", "module 9.pdf", "module 10.pdf"]

merger = PyPDF2.PdfMerger()
for filename in PdfFiles:
    PdfFile = open(filename, 'rb')
    pdfReader = PyPDF2.PdfReader(PdfFile)
    merger.append(pdfReader)
PdfFile.close()
merger.write('merged.pdf') 
