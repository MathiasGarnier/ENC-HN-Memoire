import os
from PIL import Image
from pypdf import PdfReader
from pdf2image import convert_from_path

# Cours Python Avancé CVG.

def get_pdf_page_total(pdf_path):
    reader = PdfReader(pdf_path)
    return len(reader.pages)

def convert_pdf_to_jpg(input_folder, output_folder, dpi=300, jpeg_quality=75):
    pdf_files = [f for f in os.listdir(input_folder) if f.endswith('.pdf')]
    for pdf_file in pdf_files:
        pdf_path = os.path.join(input_folder, pdf_file)
        pdf_name = os.path.splitext(pdf_file)[0]
        pdf_output_dir = os.path.join(output_folder, pdf_name)
        os.makedirs(pdf_output_dir, exist_ok=True)
        total_pages = get_pdf_page_total(pdf_path)

        images = convert_from_path(pdf_path, dpi=dpi)
        for num_page in range(1, total_pages + 1):
            output_file = os.path.join(pdf_output_dir, f"{pdf_name}_{num_page}.jpg")
            images[num_page - 1].save(output_file, quality=jpeg_quality)
