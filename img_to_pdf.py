from wand.image import Image

# Path to the PDF file
pdf_file_path = "boat invoice.pdf"

# Read PDF and convert each page to image
with Image(filename=pdf_file_path, resolution=300) as img:
    img.format = 'png'
    img.compression_quality = 90
    img.save(filename='output.png')
