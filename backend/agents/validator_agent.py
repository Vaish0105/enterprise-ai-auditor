"""
=====================================================
Agent : Validator Agent
Purpose : Validate audit findings
=====================================================
"""

import logging


logging.basicConfig(
    filename="logs/audit.log",
    level=logging.INFO
)


# Validator Node
# Validate graph output
def validator_agent(
        state
):

    errors = []

    # OCR validation
    # Ensure text exists
    if not state.get(
        "document_text"
    ):

        errors.append(
            "OCR text missing"
        )

    # Classification validation
    # Ensure document type found
    if (

        state.get(
            "document_type"
        )

        ==

        "unknown"

    ):

        errors.append(
            "Unknown document type"
        )

    # Policy validation
    # Ensure policy exists
    if not state.get(
        "policy_matches"
    ):

        errors.append(
            "No policy found"
        )

    # GPT findings validation
    # Validate evidence
    violations = state.get(
        "violations",
        []
    )

    document_text = (

        state.get(
            "document_text",
            ""
        )
        .lower()
    )

    validated_findings = []

    for finding in violations:

        # GPT structured finding
        # Check evidence
        if isinstance(
            finding,
            dict
        ):

            evidence = (

                finding.get(
                    "evidence",
                    ""
                )
                .lower()
            )

            policy = finding.get(
                "policy",
                ""
            )

            violation = finding.get(
                "violation",
                ""
            )

            # Evidence exists
            # Policy exists
            if (

                len(
                    evidence
                ) > 0

                and

                len(
                    policy
                ) > 0

            ):

                validated_findings.append(
                    finding
                )

            else:

                errors.append(

                    f"Invalid finding: {violation}"

                )

        else:

            validated_findings.append(
                finding
            )

    # Store validated findings
    # Hallucination reduction
    state[
        "validated_findings"
    ] = validated_findings

    # Validation status
    # Final result
    if len(errors) == 0:

        state[
            "validation_status"
        ] = "passed"

        logging.info(
            "Validation passed"
        )

    else:

        state[
            "validation_status"
        ] = "failed"

        logging.error(
            str(errors)
        )

    state[
        "validation_errors"
    ] = errors

    return state