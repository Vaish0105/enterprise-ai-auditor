"""
=====================================================
Page : Audit History
Purpose : View previous audits
=====================================================
"""

import pandas as pd
import gradio as gr

from backend.database.audit_history_repository import (
    get_all_audits
)


def build_audit_history():

    audits = get_all_audits()

    data = []

    for audit in audits:

        data.append(

            [
                audit.audit_id,
                audit.document_type,
                audit.risk_score,
                audit.validation_status,
                str(audit.created_at)
            ]
        )

    df = pd.DataFrame(

        data,

        columns=[

            "Audit ID",
            "Document Type",
            "Risk Score",
            "Validation Status",
            "Created At"
        ]
    )

    with gr.Column():

        gr.Markdown(
            "# Audit History"
        )

        gr.Dataframe(
            value=df,
            interactive=False
        )