"""
=====================================================
Page : Approval Dashboard
Purpose : Human approval workflow
=====================================================
"""

import pandas as pd
import gradio as gr

from backend.database.approval_repository import (
    get_pending_approvals,
    approve_audit,
    reject_audit
)


def load_approvals():

    approvals = get_pending_approvals()

    data = []

    for row in approvals:

        data.append(

            [
                row.audit_id,
                row.document_type,
                row.risk_score,
                row.approval_status
            ]
        )

    return pd.DataFrame(

        data,

        columns=[

            "Audit ID",
            "Document Type",
            "Risk Score",
            "Approval Status"
        ]
    )


def approve_action(
        audit_id
):

    approve_audit(
        int(audit_id)
    )

    return load_approvals()


def reject_action(
        audit_id
):

    reject_audit(
        int(audit_id)
    )

    return load_approvals()


def build_approval_dashboard():

    with gr.Column():

        gr.Markdown(
            "# Pending Approvals"
        )

        audit_id = gr.Number(
            label="Audit ID"
        )

        with gr.Row():

            approve_btn = gr.Button(
                "Approve"
            )

            reject_btn = gr.Button(
                "Reject"
            )

        approval_table = gr.Dataframe(
            value=load_approvals(),
            interactive=False
        )

        approve_btn.click(
            fn=approve_action,
            inputs=audit_id,
            outputs=approval_table
        )

        reject_btn.click(
            fn=reject_action,
            inputs=audit_id,
            outputs=approval_table
        )