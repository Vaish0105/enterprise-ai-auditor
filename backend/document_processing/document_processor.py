"""
=====================================================
Module : Document Processor
Purpose : Orchestrate processing pipeline
=====================================================
"""

from backend.document_processing.ocr_agent import (
    extract_text
)

from backend.document_processing.pii_detector import (
    detect_pii
)

from backend.document_processing.classifier_agent import (
    classify_document
)

from backend.document_processing.json_formatter import (
    format_document_json
)


# Process uploaded document
# Execute complete pipeline
def process_document(
        file_path
):

    # OCR extraction
    # Convert image to text
    extracted_text = extract_text(
        file_path
    )

    # PII detection
    # Identify sensitive data
    pii_findings = detect_pii(
        extracted_text
    )

    # Document classification
    # Identify document type
    document_type = classify_document(
        extracted_text
    )

    # Build structured output
    # Return JSON
    return format_document_json(
        document_type,
        extracted_text,
        pii_findings
    )