"""
=====================================================
Agent : Approval Agent
Purpose : Human approval workflow
=====================================================
"""


def approval_agent(
        state
):

    risk_score = state.get(
        "risk_score",
        0
    )

    # High risk audits
    if risk_score >= 80:

        state[
            "approval_required"
        ] = True

        state[
            "approval_status"
        ] = "pending"

    else:

        state[
            "approval_required"
        ] = False

        state[
            "approval_status"
        ] = "not_required"

    return state