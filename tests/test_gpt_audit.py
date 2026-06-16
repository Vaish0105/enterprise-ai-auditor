from backend.agents.audit_agent_gpt import (
    audit_agent_gpt
)

state = {

    "document_text":
    """
    HOTEL GRAND PALACE

    Room Charges 6000

    Taxes 1000

    Total Amount 7000
    """,

    "policy_matches":
    [

        {
            "content":
            """
            Hotel reimbursement
            limit is ₹5000.

            Manager approval
            required above ₹5000.
            """
        }
    ]
}

result = audit_agent_gpt(
    state
)

print(result)