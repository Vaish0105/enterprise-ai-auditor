"""
=====================================================
Module : JSON Formatter
Purpose : Standardized output
=====================================================
"""


# Create structured response
# Standard output format
def format_document_json(
        document_type,
        extracted_text,
        pii_findings
):

    return {

        "document_type":
        document_type,

        "pii_findings":
        pii_findings,

        "raw_text":
        extracted_text
    }