from io import BytesIO

import pymupdf  # pip install PyMuPDF
import requests  # pip install requests

online = False

if online is True:
    pdfStream = requests.get(
        'https://pycon-assets.s3.amazonaws.com/2024/media/'
        'documents/DLCC-Floorplan-Marked_up_PyCon_US_2024.pdf').content
else:
    pdfStream = BytesIO(
        open('DLCC-Floorplan-Marked_up_PyCon_US_2024.pdf', 'rb').read())

for (n, page) in enumerate(pymupdf.Document(stream=pdfStream).pages(), 1):
    imageFilename = f'page-{n}.png'
    print(f'Converting page {n} to "{imageFilename}"…')
    page.get_pixmap(dpi=300).save(imageFilename)
