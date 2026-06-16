from backend.agents.validator_agent import (
    validator_agent
)

state = {

    "document_text":
    "Total Amount 7000",

    "document_type":
    "hotel_invoice",

    "policy_matches":
    [

        {
            "content":
            "Hotel limit 5000"
        }
    ],

    "violations":
    [

        {
            "policy":
            "Hotel limit 5000",

            "violation":
            "Limit exceeded",

            "evidence":
            "Total Amount 7000"
        }
    ]
}

result = validator_agent(
    state
)

print(result)