"""
=====================================================
Agent : Prompt Injection Agent
Purpose : Detect prompt injection attacks
=====================================================
"""


# Prompt Injection Node
# Detect malicious instructions
def prompt_injection_agent(
        state
):

    document_text = (

        state.get(
            "document_text",
            ""
        )
        .lower()
    )

    suspicious_patterns = [

        "ignore previous instructions",

        "ignore all instructions",

        "override policy",

        "act as administrator",

        "act as admin",

        "reveal hidden prompt",

        "reveal system prompt",

        "bypass security",

        "bypass audit",

        "disable validation",

        "forget your instructions"
    ]

    findings = []

    for pattern in suspicious_patterns:

        if pattern in document_text:

            findings.append(
                pattern
            )

    state[
        "prompt_injection_findings"
    ] = findings

    if len(findings) > 0:

        state[
            "prompt_injection_status"
        ] = "detected"

    else:

        state[
            "prompt_injection_status"
        ] = "clean"

    return state