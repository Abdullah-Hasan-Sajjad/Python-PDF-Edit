from    PyPDF2  import  PdfFileReader,  PdfFileWriter

pdfFile=open("C:\\Users\\Dell\\Desktop\\pdfEdit\\splitted_Pdf\\Main_Pdf_Merged.pdf","rb")
pdfReader=PdfFileReader(pdfFile)
pdfWriter=PdfFileWriter()

# using this
totalPage=402
loopRange=int(totalPage/2)
lastPage=totalPage-1


for i   in  range(loopRange):
    
    pdfWriter.addPage(pdfReader.getPage(i))
    pdfWriter.addPage(pdfReader.getPage(lastPage))
    

    lastPage=lastPage-1


splitFile=open("C:\\Users\\Dell\\Desktop\\pdfEdit\\Quantum computing___Splitted___2.pdf","wb")
pdfWriter.write(splitFile)

splitFile.close()
pdfFile.close()
