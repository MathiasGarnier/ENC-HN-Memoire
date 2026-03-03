import fitz  # PyMuPDF
from PIL import Image
from surya.recognition import RecognitionPredictor
from surya.detection import DetectionPredictor
import os

def pdf_to_png(pdf_path, output_folder="pdf_images", dpi=300):
    """
    Converts each page of a PDF into a separate PNG image.

    Args:
        pdf_path (str): The path to the input PDF file.
        output_folder (str): The folder where the PNG images will be saved.
                             Defaults to "pdf_images".
        dpi (int): The DPI (Dots Per Inch) for the output images. Higher DPI
                   results in higher quality but larger file sizes.
                   Defaults to 300.
    """
    if not os.path.exists(pdf_path):
        print(f"Error: PDF file not found at '{pdf_path}'")
        return

    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    try:
        # Open the PDF document
        document = fitz.open(pdf_path)
        print(f"Opened PDF: {pdf_path}")

        # Calculate the zoom factor based on DPI
        # Default rendering is at 72 DPI. To get 300 DPI, we need a zoom of 300/72.
        zoom = dpi / 72
        mat = fitz.Matrix(zoom, zoom) # Transformation matrix for rendering

        for page_num in range(len(document)):
            page = document.load_page(page_num)  # Load a specific page

            # Render page to a pixmap (pixel map) with the specified matrix
            pix = page.get_pixmap(matrix=mat)

            # Define the output PNG filename
            output_filename = os.path.join(output_folder, f"page_{page_num + 1}.png")

            # Save the pixmap as a PNG image
            pix.save(output_filename)
            print(f"Generated {output_filename}")

        document.close()
        print(f"Successfully converted all pages of '{pdf_path}' to PNGs in '{output_folder}'")

    except fitz.FileNotFoundError:
        print(f"Error: PDF file not found at '{pdf_path}'")
    except Exception as e:
        print(f"An error occurred: {e}")

# if __name__ == "__main__":
#     # --- How to use the script ---

#     # 1. IMPORTANT: Install PyMuPDF
#     #    pip install PyMuPDF

#     # Example Usage:
#     input_pdf = "C:\\Users\\mathi\\OneDrive\\Bureau\\Bourbaki\\test OCR\\redac 1.pdf"  # <--- REPLACE WITH YOUR PDF FILE PATH
#     output_directory = "C:\\Users\\mathi\\OneDrive\\Bureau\\Bourbaki\\test OCR" # <--- OPTIONAL: Change output folder name
#     desired_dpi = 300                 # <--- OPTIONAL: Change DPI for quality

#     # Create a dummy PDF for demonstration if it doesn't exist
#     if not os.path.exists(input_pdf):
#         print(f"Creating a dummy PDF '{input_pdf}' for demonstration purposes.")
#         try:
#             doc = fitz.open()  # new PDF
#             doc.new_page()
#             doc.insert_text(fitz.Point(50, 100), "This is page 1 of the dummy PDF.", fontname="helv", fontsize=20)
#             doc.new_page()
#             doc.insert_text(fitz.Point(50, 100), "This is page 2 with some more text.", fontname="helv", fontsize=20)
#             doc.save(input_pdf)
#             doc.close()
#             print(f"Dummy PDF '{input_pdf}' created. Running conversion...")
#         except Exception as e:
#             print(f"Could not create dummy PDF: {e}. Please ensure you have PyMuPDF installed.")
#             print(f"Please provide your own PDF file named '{input_pdf}' in the same directory.")
#             exit()

#     pdf_to_png(input_pdf, output_directory, desired_dpi)

image = Image.open("C:\\Users\\mathi\\OneDrive\\Bureau\\DH\\Bourbaki0 OCR non\\test_OCR\\test2.png")
recognition_predictor = RecognitionPredictor()
detection_predictor = DetectionPredictor()

predictions = recognition_predictor([image], det_predictor=detection_predictor)

if predictions:
    # Assuming predictions[0] is the list of results for the first image
    image_predictions = predictions[0]

    for pred in image_predictions:
        # Check if 'pred' is a tuple, which the error suggests
        if isinstance(pred, tuple) and len(pred) >= 2:
            bbox = pred[0]  # The first element is likely the bounding box
            text = pred[1]  # The second element is likely the recognized text

            print(f"Texte: {text}")
            print(f"Boîte englobante (bbox): {bbox}")
            print("-" * 20)
        else:
            print(f"Format de prédiction inattendu: {pred}")
            print("-" * 20)
else:
    print("Aucune prédiction n'a été retournée pour l'image.")
