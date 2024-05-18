from io import BytesIO

import pymupdf  # pip install PyMuPDF
import requests  # pip install requests

online = True

if online:
    filestream = requests.get(
        'https://pycon-assets.s3.amazonaws.com/2024/media/'
        'documents/DLCC-Floorplan-Marked_up_PyCon_US_2024.pdf').content
else:
    with open('DLCC-Floorplan-Marked_up_PyCon_US_2024.pdf', 'rb') as fh:
        filestream = BytesIO(fh.read())

doc = pymupdf.Document(stream=filestream)

for (pageNumber, page) in enumerate(doc.pages()):
    imageFilename = f'page-{pageNumber + 1}.png'
    print(f'Converting page {pageNumber + 1} to "{(imageFilename)}"…')
    pixmap = page.get_pixmap(dpi=300)
    pixmap.save(imageFilename)
