import sys
import os
from pdfminer.pdfinterp import PDFResourceManager,PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from openpyxl import Workbook

#main
def main(argv) :
    outfile = argv[1] + '.txt'
    args = [argv[1]]

    debug = 0
    pagenos = set()
    password = ''
    maxpages = 0
    rotation = 0
    codec = 'utf-8' 
    caching = True
    imagewriter = None
    laparams = LAParams()
    #
    PDFResourceManager.debug = debug
    PDFPageInterpreter.debug = debug

    rsrcmgr = PDFResourceManager(caching=caching)
    outfp = file(outfile,'w')
    device = TextConverter(rsrcmgr, outfp, codec=codec, laparams=laparams,
                imagewriter=imagewriter)
    for fname in args:
        fp = file(fname,'rb')
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        for page in PDFPage.get_pages(fp, pagenos,
                          maxpages=maxpages, password=password,
                          caching=caching, check_extractable=True) :
            page.rotate = (page.rotate+rotation) % 360
            interpreter.process_page(page)
        fp.close()
    device.close()
    outfp.close()

    wb = Workbook()
    ws = wb.active
 

    outfp = file(outfile,'r')
    result = []
    while True:
        line = outfp.readline()
        if "Ticket Number" in line:
            temp = line.split(' ')
            result.append(temp[-1][0:-1])
        if "Date of Issue" in line:
            line = outfp.readline()
            line = outfp.readline()
            temp = line.split(' ')
            result.append(temp[-1][0:-1])
            line = outfp.readline()
            line = outfp.readline()
            temp = line.split(' ')
            result.append(temp[-1][0:-1])
            print result
        if len(result) == 3:
            ws.append(result)
            result = []
        if not line:
            break
    outfp.close()
    wb.save(argv[1] + '.xlsx')

    return
if __name__ == '__main__' : main(sys.argv)
