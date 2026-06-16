import json

from sqlalchemy import text

from backend.database.postgres import (
    engine
)


def save_audit_result(
        state
):

    with engine.connect() as conn:
        conn.execute(
    text(
        """
        INSERT INTO audit_history (

            document_type,

            risk_score,

            validation_status,

            violations,

            approval_required,

            approval_status

        )

        VALUES (

            :document_type,

            :risk_score,

            :validation_status,

            :violations,

            :approval_required,

            :approval_status

        )
        """
    ),

    {

        "document_type":
        state.get(
            "document_type"
        ),

        "risk_score":
        state.get(
            "risk_score"
        ),

        "validation_status":
        state.get(
            "validation_status"
        ),

        "violations":
        json.dumps(
            state.get(
                "violations",
                []
            )
        ),

        "approval_required":
        state.get(
            "approval_required",
            False
        ),

        "approval_status":
        state.get(
            "approval_status",
            "not_required"
        )
    }
)

        conn.commit()