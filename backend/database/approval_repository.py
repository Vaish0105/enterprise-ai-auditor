"""
=====================================================
Module : Approval Repository
Purpose : Fetch pending approvals
=====================================================
"""

from sqlalchemy import text

from backend.database.postgres import (
    engine
)


def get_pending_approvals():

    with engine.connect() as conn:

        result = conn.execute(
            text(
                """
                SELECT

                    audit_id,

                    document_type,

                    risk_score,

                    approval_status

                FROM audit_history

                WHERE approval_required = TRUE

                ORDER BY audit_id DESC
                """
            )
        )

        return result.fetchall()


def approve_audit(
        audit_id
):

    with engine.connect() as conn:

        conn.execute(
            text(
                """
                UPDATE audit_history

                SET approval_status = 'approved'

                WHERE audit_id = :audit_id
                """
            ),
            {
                "audit_id": audit_id
            }
        )

        conn.commit()


def reject_audit(
        audit_id
):

    with engine.connect() as conn:

        conn.execute(
            text(
                """
                UPDATE audit_history

                SET approval_status = 'rejected'

                WHERE audit_id = :audit_id
                """
            ),
            {
                "audit_id": audit_id
            }
        )

        conn.commit()