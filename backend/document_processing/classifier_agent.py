"""
=====================================================
Module : Classifier Agent
Purpose : Classify document type
=====================================================
"""


# Determine document type
# Rule-based MVP version
def classify_document(
        text
):

    text = text.lower()

    # Hotel document
    # Check hotel keywords
    if "hotel" in text:

        return "hotel_invoice"

    # Flight document
    # Check airline keywords
    if "flight" in text:

        return "flight_ticket"

    # Taxi document
    # Check transport keywords
    if "taxi" in text:

        return "taxi_receipt"

    return "unknown"