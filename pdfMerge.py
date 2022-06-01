from PyPDF2 import PdfFileMerger

path="C:\\Users\\Dell\\Desktop\\pdfEdit\\splitted_Pdf\\"
name="Quantum computingMain_"
pdfS = []

for i   in  range(1,403):

    pdfS.append(path+name+str(i)+"-"+str(i)+".pdf")

merger = PdfFileMerger()

for pdf in pdfS:
    merger.append(pdf)

merger.write("C:\\Users\\Dell\\Desktop\\pdfEdit\\splitted_Pdf\\Main_Pdf_Merged.pdf")
merger.close()
