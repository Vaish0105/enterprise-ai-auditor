"""
=====================================================
Page : Auditor Dashboard
=====================================================
"""

import gradio as gr


# Auditor workspace
# Shows audit-related actions
def auditor_dashboard():

    with gr.Column():

        gr.Markdown(
            "#  Auditor Dashboard"
        )

        with gr.Row():

            gr.Number(
                value=18,
                label="Pending Reviews"
            )

            gr.Number(
                value=4,
                label="Fraud Alerts"
            )

        gr.Button(
            "Review Claims"
        )

        gr.Button(
            "Fraud Investigation"
        )

        gr.Button(
            "Audit Reports"
        )