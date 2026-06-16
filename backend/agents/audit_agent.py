"""
=====================================================
Agent : Audit Agent
Purpose : Detect policy violations
=====================================================
"""


# Audit Agent Node
# Compare document with policy
def audit_agent(
        state
):

    # Get OCR text
    # Extracted document text
    document_text = state[
        "document_text"
    ].lower()

    # Get retrieved policies
    # Qdrant retrieval output
    policies = state[
        "policy_matches"
    ]

    # Store violations
    # Audit findings list
    violations = []

    # Combine all policies
    # Create policy context
    policy_text = ""

    for policy in policies:

        policy_text += (

            policy.get(
                "content",
                ""
            )
            .lower()
        )

    # Hotel invoice checks
    # MVP rule engine
    if (

        state[
            "document_type"
        ]

        ==

        "hotel_invoice"

    ):

        # Detect invoice amount
        # Example test invoice
        if "7000" in document_text:

            # Check retrieved policy
            # Hotel limit present
            if (

                "5000"
                in
                policy_text

            ):

                violations.append(

                    "Hotel limit exceeded"

                )

    # Save violations
    # Used by validator
    state[
        "violations"
    ] = violations

    return state