from backend.database.audit_repository import (
    save_audit_result
)

state = {

    "document_type":
    "hotel_invoice",

    "risk_score":
    75,

    "validation_status":
    "passed",

    "violations":
    [

        "Hotel limit exceeded",

        "Manager approval required"
    ]
}

save_audit_result(
    state
)

print(
    "Audit Saved"
)