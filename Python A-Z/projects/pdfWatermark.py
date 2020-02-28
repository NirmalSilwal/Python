import PyPDF2

template = PyPDF2.PdfFileReader(open('pdfs/super.pdf','rb'))

watermark = PyPDF2.PdfFileReader(open('pdfs/wtr.pdf','rb'))

writer = PyPDF2.PdfFileWriter()

# print(template.getNumPages())
for i in range(template.getNumPages()):
    current_page = template.getPage(i)
    current_page.mergePage(watermark.getPage(0))
    writer.addPage(current_page)

    with open('pdfs/watermarked_file.pdf','wb') as opfile:
        writer.write(opfile)