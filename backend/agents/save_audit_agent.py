"""
=====================================================
Agent : Save Audit Agent
Purpose : Save audit results to PostgreSQL
=====================================================
"""

from backend.database.audit_repository import (
    save_audit_result
)


def save_audit_agent(
        state
):

    save_audit_result(
        state
    )

    return state