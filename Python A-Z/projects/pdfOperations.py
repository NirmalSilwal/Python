import PyPDF2

with open('./pdfs/dummy.pdf','rb') as ipfile:
    reader = PyPDF2.PdfFileReader(ipfile)
    # print(reader.numPages)
    # print(reader.getPage(0))
    page = reader.getPage(0)
    page.rotateClockwise(90)
    writer = PyPDF2.PdfFileWriter()
    writer.addPage(page)
    with open('./pdfs/tilt.pdf','wb') as opfile:
        writer.write(opfile)