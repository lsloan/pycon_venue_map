import urllib.request

import pymupdf  # pip install PyMuPDF

url = ('https://pycon-assets.s3.amazonaws.com/2024/media/'
       'documents/DLCC-Floorplan-Marked_up_PyCon_US_2024.pdf')
# url = 'file:DLCC-Floorplan-Marked_up_PyCon_US_2024.pdf'

with urllib.request.urlopen(url) as response:
    pdfStream = response.read()

for (n, page) in enumerate(pymupdf.Document(stream=pdfStream).pages(), 1):
    imageFilename = f'page-{n}.png'
    print(f'Converting page {n} to "{imageFilename}"…')
    page.get_pixmap(dpi=300).save(imageFilename)
