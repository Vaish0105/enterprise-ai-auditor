"""
=====================================================
Page : Audit Search
Purpose : Search audit records
=====================================================
"""

import pandas as pd
import gradio as gr

from backend.database.search_repository import (
    search_audits
)


def run_search(
        document_type,
        approval_status,
        min_risk
):

    results = search_audits(

        document_type,

        approval_status,

        min_risk
    )

    data = []

    for row in results:

        data.append(

            [
                row.audit_id,
                row.document_type,
                row.risk_score,
                row.approval_status,
                str(row.created_at)
            ]
        )

    return pd.DataFrame(

        data,

        columns=[

            "Audit ID",

            "Document Type",

            "Risk Score",

            "Approval Status",

            "Created At"
        ]
    )


def build_audit_search_page():

    with gr.Column():

        gr.Markdown(
            "# 🔍 Audit Search"
        )

        document_type = gr.Textbox(
            label="Document Type"
        )

        approval_status = gr.Dropdown(

            choices=[

                "",
                "pending",
                "approved",
                "rejected"
            ],

            value="",

            label="Approval Status"
        )

        min_risk = gr.Number(

            value=0,

            label="Minimum Risk Score"
        )

        search_button = gr.Button(
            "Search"
        )

        results = gr.Dataframe()

        search_button.click(

            fn=run_search,

            inputs=[

                document_type,

                approval_status,

                min_risk
            ],

            outputs=results
        )