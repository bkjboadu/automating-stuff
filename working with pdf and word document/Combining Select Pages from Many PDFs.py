import PyPDF2
from pathlib import Path

pdf = []
for file in Path.cwd().glob('*.pdf'):
    pdf.append(file)

finished = open('done.pdf','wb')
newpdf = PyPDF2.PdfFileWriter()
for file in pdf:
    files = open(file,'rb')
    pdfreader = PyPDF2.PdfFileReader(files)
    if pdfreader.isEncrypted:
        pdfreader.decrypt('bright')
    else:
        pass

    for pageNum in range(1,pdfreader.numPages):
        newpdf.addPage(pdfreader.getPage(pageNum))


newpdf.write(finished)









