#!/usr/bin/env python
# -*- coding: utf-8 -*-

from urllib.request import urlopen
from pdfminer.pdfinterp import PDFResourceManager, process_pdf
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from io import StringIO

def readPDF(path):
   rsrcmgr = PDFResourceManager()
   retstr = StringIO()
   laparams = LAParams()
   device = TextConverter(rsrcmgr, retstr, laparams=laparams)

   process_pdf(rsrcmgr, device, path)
   device.close()

   content = retstr.getvalue()
   retstr.close()
   return content

path = urlopen("http://pythonscraping.com/pages/warandpeace/chapter1.pdf")
outputString = readPDF(path)
print(outputString)
path.close()