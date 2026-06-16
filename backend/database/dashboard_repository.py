"""
=====================================================
Module : Dashboard Repository
Purpose : Dashboard metrics
=====================================================
"""

from sqlalchemy import text

from backend.database.postgres import (
    engine
)


def get_total_audits():

    with engine.connect() as conn:

        result = conn.execute(
            text(
                """
                SELECT COUNT(*)
                FROM audit_history
                """
            )
        )

        return result.scalar()


def get_average_risk():

    with engine.connect() as conn:

        result = conn.execute(
            text(
                """
                SELECT COALESCE(
                    AVG(risk_score),
                    0
                )
                FROM audit_history
                """
            )
        )

        return round(
            float(
                result.scalar()
            ),
            2
        )


def get_failed_validations():

    with engine.connect() as conn:

        result = conn.execute(
            text(
                """
                SELECT COUNT(*)
                FROM audit_history
                WHERE validation_status='failed'
                """
            )
        )

        return result.scalar()


def get_total_policies():

    return 1

def get_risk_distribution():

    with engine.connect() as conn:

        low = conn.execute(
            text(
                """
                SELECT COUNT(*)
                FROM audit_history
                WHERE risk_score < 50
                """
            )
        ).scalar()

        medium = conn.execute(
            text(
                """
                SELECT COUNT(*)
                FROM audit_history
                WHERE risk_score >= 50
                AND risk_score < 80
                """
            )
        ).scalar()

        high = conn.execute(
            text(
                """
                SELECT COUNT(*)
                FROM audit_history
                WHERE risk_score >= 80
                """
            )
        ).scalar()

        return {

            "Low": low,

            "Medium": medium,

            "High": high
        }

def get_pending_approvals():

        with engine.connect() as conn:

            result = conn.execute(
                text(
                    """
                    SELECT COUNT(*)
                    FROM audit_history
                    WHERE approval_status='pending'
                    """
                )
            )

            return result.scalar()
        
def get_high_risk_audits():

    with engine.connect() as conn:

        result = conn.execute(
            text(
                """
                SELECT COUNT(*)
                FROM audit_history
                WHERE risk_score >= 80
                """
            )
        )

        return result.scalar()
    
def get_approval_rate():

    with engine.connect() as conn:

        approved = conn.execute(
            text(
                """
                SELECT COUNT(*)
                FROM audit_history
                WHERE approval_status='approved'
                """
            )
        ).scalar()

        total = conn.execute(
            text(
                """
                SELECT COUNT(*)
                FROM audit_history
                WHERE approval_required=TRUE
                """
            )
        ).scalar()

        if total == 0:

            return 0

        return round(
            (approved / total) * 100,
            2
        )
    
def get_approved_audits():

    with engine.connect() as conn:

        result = conn.execute(
            text(
                """
                SELECT COUNT(*)
                FROM audit_history
                WHERE approval_status='approved'
                """
            )
        )

        return result.scalar()
    
def get_rejected_audits():

    with engine.connect() as conn:

        result = conn.execute(
            text(
                """
                SELECT COUNT(*)
                FROM audit_history
                WHERE approval_status='rejected'
                """
            )
        )

        return result.scalar()