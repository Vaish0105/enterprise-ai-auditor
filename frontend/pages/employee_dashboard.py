"""
=====================================================
Page : Employee Dashboard
=====================================================
"""

import gradio as gr


# Employee workspace
# Claim submission portal
def employee_dashboard():

    with gr.Column():

        gr.Markdown(
            "#  Employee Dashboard"
        )

        gr.Button(
            "Upload Claim"
        )

        gr.Button(
            "View Claim Status"
        )

        gr.Button(
            "Audit Reports"
        )

        gr.Button(
            "Chat With Auditor"
        )