"""
=====================================================
Agent : Risk Agent
Purpose : Generate risk score
=====================================================
"""


# Risk Node
# Generate risk score
def risk_agent(
        state
):

    violations = state.get(
        "violations",
        []
    )

    count = len(
        violations
    )

    if count == 0:

        score = 10

    elif count == 1:

        score = 50

    else:

        score = 90

    state[
        "risk_score"
    ] = score

    return state