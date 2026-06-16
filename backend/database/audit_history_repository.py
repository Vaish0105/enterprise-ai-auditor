from sqlalchemy import text
from backend.database.postgres import engine


def get_all_audits():

    with engine.connect() as conn:

        result = conn.execute(
            text(
                """
                SELECT
                    audit_id,
                    document_type,
                    risk_score,
                    validation_status,
                    created_at
                FROM audit_history
                ORDER BY audit_id DESC
                """
            )
        )

        return result.fetchall()