"""
=====================================================
Graph State
=====================================================
"""

from typing import TypedDict


class AuditState(
    TypedDict,
    total=False
):

    file_path: str

    document_text: str

    document_type: str

    pii_findings: list

    policy_matches: list

    violations: list

    validation_status: str

    validation_errors: list


    risk_score: int

    audit_report: str

    approval_required: bool
    approval_status: str