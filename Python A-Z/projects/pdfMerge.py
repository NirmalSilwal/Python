import PyPDF2
import sys

# pdf1 = sys.argv[1]
# pdf2 = sys.argv[2]

inputs = sys.argv[1:]

def pdf_combiner(pdf_list):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        print(pdf)
        merger.append(pdf)
    merger.write('./pdfs/super.pdf')

pdf_combiner(inputs)

# run similar command like below from the terminal
# >python pdfMerge.py pdfs/dummy.pdf pdfs/twopage.pdf pdfs/tilt.pdf