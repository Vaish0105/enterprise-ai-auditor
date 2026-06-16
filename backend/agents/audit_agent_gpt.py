"""
=====================================================
Agent : GPT Audit Agent
Purpose : LLM-based policy auditing
=====================================================
"""

import json

from openai import (
    OpenAI
)

from backend.config.settings import (
    settings
)


client = OpenAI(

    api_key=
    settings.OPENAI_API_KEY
)


def audit_agent_gpt(
        state
):

    document_text = state[
        "document_text"
    ]

    policies = state[
        "policy_matches"
    ]

    policy_text = "\n\n".join(

        [
            p["content"]

            for p

            in policies
        ]
    )

    prompt = f"""

You are an enterprise AI Auditor.

Document:

{document_text}

Policies:

{policy_text}

Analyze the document against the policies.

Return ONLY valid JSON.

Format:

{{
    "violations": [],
    "reasoning": [],
    "risk_score": 0
}}

Rules:

1. Return valid JSON only.
2. Do not include markdown.
3. Do not include explanations outside JSON.
4. Risk score must be between 0 and 100.
5. Include all policy violations found.
6. Explain reasoning using evidence from the document and policies.

"""

    response = client.chat.completions.create(

        model=
        "gpt-5.5",

        messages=[

            {
                "role":
                "user",

                "content":
                prompt
            }
        ]
    )

    result = response.choices[
        0
    ].message.content

    try:

        audit_result = json.loads(
            result
        )

    except Exception:

        audit_result = {

            "violations": [],

            "reasoning": [
                result
            ],

            "risk_score": 0
        }

    state[
        "violations"
    ] = audit_result.get(
        "violations",
        []
    )

    state[
        "reasoning"
    ] = audit_result.get(
        "reasoning",
        []
    )

    state[
        "risk_score"
    ] = audit_result.get(
        "risk_score",
        0
    )

    return state