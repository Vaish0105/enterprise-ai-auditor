"""
=====================================================
Page : Admin Dashboard
Purpose : Admin Control Center
=====================================================
"""

import gradio as gr


# Build admin dashboard
# Visible after successful login
def admin_dashboard():

    with gr.Column():

        # Dashboard title
        # Show role information
        gr.Markdown(
            "# Enterprise AI Auditor"
        )

        # Welcome message
        # Admin landing page
        gr.Markdown(
            "## Welcome System Admin"
        )

        # KPI cards row
        # Placeholder values
        with gr.Row():

            gr.Number(
                value=15,
                label="Users"
            )

            gr.Number(
                value=23,
                label="Pending Audits"
            )

            gr.Number(
                value=4,
                label="Fraud Alerts"
            )

            gr.Number(
                value=12,
                label="Policies"
            )

        # Navigation section
        # Future functionality
        gr.Button(
            "User Management"
        )

        gr.Button(
            " Policy Management"
        )

        gr.Button(
            " Governance Dashboard"
        )

        gr.Button(
            "Audit Monitoring"
        )

        # Logout button
        # End user session
        gr.Button(
            " Logout"
        )