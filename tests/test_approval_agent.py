from backend.agents.approval_agent import (
    approval_agent
)

state = {

    "risk_score": 90
}

result = approval_agent(
    state
)

print(result)