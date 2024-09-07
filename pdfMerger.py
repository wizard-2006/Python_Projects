import PyPDF2
merger=PyPDF2.PdfMerger()
files=["pdf1.pdf","pdf2.pdf"]
for file in files:
    pdfFile=open(file,'rb')
    pdfReader=PyPDF2.PdfReader(pdfFile)
    merger.append(pdfReader)
pdfFile.close()
merger.write("merged.pdf")

