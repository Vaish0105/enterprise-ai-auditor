from sqlalchemy import text

from backend.database.postgres import (
    engine
)


def search_audits(
        document_type,
        approval_status,
        min_risk
):

    query = """
    SELECT

        audit_id,

        document_type,

        risk_score,

        approval_status,

        created_at

    FROM audit_history

    WHERE 1=1
    """

    params = {}

    if document_type:

        query += """

        AND document_type = :document_type
        """

        params[
            "document_type"
        ] = document_type

    if approval_status:

        query += """

        AND approval_status = :approval_status
        """

        params[
            "approval_status"
        ] = approval_status

    query += """

    AND risk_score >= :min_risk

    ORDER BY audit_id DESC
    """

    params[
        "min_risk"
    ] = min_risk

    with engine.connect() as conn:

        result = conn.execute(
            text(query),
            params
        )

        return result.fetchall()