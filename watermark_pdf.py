import PyPDF2
import sys
import os

#input = sys.argv[1:]
pdf_file = PyPDF2.PdfFileReader(open('twopage.pdf', 'rb'))
watermark = PyPDF2.PdfFileReader(open('watermark.pdf', 'rb'))
output = PyPDF2.PdfFileWriter()

for i in range(pdf_file.getNumPages()):
    page = pdf_file.getPage(i)
    page.mergePage(watermark.getPage(0))
    output.addPage(page)
    with open('waterfin.pdf', 'wb') as file:
        output.write(file)
