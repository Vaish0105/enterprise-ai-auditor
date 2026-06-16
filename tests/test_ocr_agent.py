from backend.agents.ocr_agent import (
    ocr_agent
)

state = {

    "file_path":
    "test_files/hotel_invoice.jpg"
}

result = ocr_agent(
    state
)

print(
    result[
        "document_text"
    ]
)