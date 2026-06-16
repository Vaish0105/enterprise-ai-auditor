from backend.agents.policy_agent import (
    policy_agent
)

state = {

    "document_type":
    "hotel_invoice"
}

result = policy_agent(
    state
)

print(
    result
)