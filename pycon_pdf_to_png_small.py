import urllib.request

import pymupdf

doc = pymupdf.Document(stream=urllib.request.urlopen(
    'https://pycon-assets.s3.amazonaws.com/2024/media/'
    'documents/DLCC-Floorplan-Marked_up_PyCon_US_2024.pdf').read())

for (n, page) in enumerate(doc.pages()):
    page.get_pixmap(dpi=300).save(f'page-{n + 1}.png')
