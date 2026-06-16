"""
=====================================================
Module : OCR Agent
Purpose : Extract text from document
=====================================================
"""

from paddleocr import PaddleOCR


# Initialize OCR engine
# Load once during startup
ocr_engine = PaddleOCR(
    use_angle_cls=True,
    lang="en"
)


# Extract text
# Return combined OCR output
def extract_text(
        image_path
):

    # Run OCR
    # Process uploaded image
    result = ocr_engine.ocr(
        image_path
    )

    extracted_text = []

    # Parse OCR output
    # Collect text lines
    for line in result[0]:

        extracted_text.append(
            line[1][0]
        )

    return "\n".join(
        extracted_text
    )