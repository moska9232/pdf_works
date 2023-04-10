import PyPDF2
import sys
import os

input = sys.argv[1:]

def pdf_combin(pdf_list):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        print(pdf)
        merger.append(pdf)
    merger.write('super.pdf')

pdf_combin(input)