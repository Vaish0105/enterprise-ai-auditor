from backend.agents.policy_agent import (
    policy_agent
)

from backend.agents.audit_agent_gpt import (
    audit_agent_gpt
)

state = {

    "document_type":
    "hotel_invoice",

    "document_text":
    """
    HOTEL GRAND PALACE

    Room Charges 6000

    Taxes 1000

    Total Amount 7000
    """
}

state = policy_agent(
    state
)

state = audit_agent_gpt(
    state
)

print("\nFINAL GPT AUDIT\n")

print(state)