"""
=====================================================
Agent : OCR Agent
Purpose : Extract text from document
=====================================================
"""


def ocr_agent(
        state
):

    # Temporary OCR mock
    # Replace with PaddleOCR later

    extracted_text = """
    HOTEL GRAND PALACE

    Invoice Number INV001

    Room Charges 6000

    Taxes 1000

    Total Amount 7000
    """

    state[
        "document_text"
    ] = extracted_text

    return state