from pdf2image import convert_from_path
pages = convert_from_path('C:\phytonProjects\stepik-certificate-67-c5baffb.pdf', 500)

for page in pages:
    page.save('C:\phytonProjects\certificate.jpg', 'JPEG')