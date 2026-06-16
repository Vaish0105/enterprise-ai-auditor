from backend.reports.pdf_generator import (
    generate_audit_pdf
)

state = {

    "document_type":
    "hotel_invoice",

    "risk_score":
    90,

    "validation_status":
    "passed",

    "violations":
    [

        "Hotel reimbursement limit exceeded",

        "Manager approval missing"
    ]
}

file = generate_audit_pdf(

    state,

    "audit_report.pdf"
)

print(file)