"""
=====================================================
Agent : Report Agent
Purpose : Generate final report
=====================================================
"""

import json


# Report Node
# Build audit report
def report_agent(
        state
):

    report = {

        "document_type":
        state.get(
            "document_type"
        ),

        "violations":
        state.get(
            "violations"
        ),

        "risk_score":
        state.get(
            "risk_score"
        ),

        "validation_status":
        state.get(
            "validation_status"
        )
    }

    state[
        "audit_report"
    ] = json.dumps(
        report,
        indent=4
    )

    return state