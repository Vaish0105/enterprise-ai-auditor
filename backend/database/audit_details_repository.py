from sqlalchemy import text

from backend.database.postgres import (
    engine
)


def get_audit_details(
        audit_id
):

    with engine.connect() as conn:

        result = conn.execute(
            text(
                """
                SELECT *
                FROM audit_history
                WHERE audit_id = :audit_id
                """
            ),
            {
                "audit_id": audit_id
            }
        )

        return result.fetchone()