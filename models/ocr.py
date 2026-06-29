import easyocr
import re

class OCRReader:

    def __init__(self):
        # Load EasyOCR once when the application starts
        self.reader = easyocr.Reader(['en'], gpu=False)

    def read_plate(self, plate_image):
        """
        Reads text from a cropped number plate image.
        Returns the detected vehicle number or None.
        """

        results = self.reader.readtext(plate_image)

        plate_number = ""

        for result in results:
            text = result[1]
            plate_number += text

        # Remove spaces and special characters
        plate_number = plate_number.upper()
        plate_number = re.sub(r'[^A-Z0-9]', '', plate_number)

        if len(plate_number) >= 6:
            return plate_number

        return None


# Create a global OCR object
ocr = OCRReader()
