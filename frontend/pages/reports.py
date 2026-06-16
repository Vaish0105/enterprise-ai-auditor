"""
=====================================================
Page : Reports
Purpose : Audit Reports
=====================================================
"""

import gradio as gr


# Build reports page
# Audit report center
def build_reports_page():

    with gr.Column():

        # Reports title
        # Audit reporting
        gr.Markdown(
            "# Reports"
        )

        # Placeholder reports
        # Real reports later
        gr.Markdown(
            """
            Available Reports

            - Monthly Audit Summary
            - Travel Spend Analysis
            - Compliance Report
            """
        )