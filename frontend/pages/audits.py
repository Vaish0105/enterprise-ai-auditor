"""
=====================================================
Page : Audit Workspace
Purpose : Audit Operations
=====================================================
"""

import gradio as gr


# Build audit workspace
# Future LangGraph area
def build_audit_workspace():

    with gr.Column():

        # Workspace title
        # Audit processing page
        gr.Markdown(
            "# Audit Workspace"
        )

        # Placeholder audit queue
        # Real data later
        gr.Dataframe(
            headers=[
                "Claim ID",
                "Type",
                "Risk Score",
                "Status"
            ],
            value=[
                ["TRV001", "Travel", 72, "Review"],
                ["TRV002", "Hotel", 18, "Approved"]
            ]
        )