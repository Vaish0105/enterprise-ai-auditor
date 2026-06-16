"""
=====================================================
Page : Dashboard
Purpose : Executive Dashboard
=====================================================
"""

import pandas as pd
import gradio as gr

from backend.database.dashboard_repository import (

    get_total_audits,

    get_average_risk,

    get_failed_validations,

    get_total_policies,

    get_risk_distribution,

    get_pending_approvals,

    get_high_risk_audits,

    get_approval_rate,

    get_approved_audits,

    get_rejected_audits
)


def get_dashboard_data():

    return [

        get_total_audits(),

        get_high_risk_audits(),

        get_pending_approvals(),

        get_approval_rate(),

        get_average_risk(),

        get_failed_validations(),

        get_total_policies()
    ]


def build_dashboard():

    total_audits = get_total_audits()

    average_risk = get_average_risk()

    failed_validations = get_failed_validations()

    total_policies = get_total_policies()

    high_risk = get_high_risk_audits()

    pending = get_pending_approvals()

    approval_rate = get_approval_rate()

    approved = get_approved_audits()

    rejected = get_rejected_audits()

    risk_data = get_risk_distribution()

    risk_df = pd.DataFrame(
        {
            "Risk Level": [
                "Low",
                "Medium",
                "High"
            ],
            "Count": [
                risk_data["Low"],
                risk_data["Medium"],
                risk_data["High"]
            ]
        }
    )

    approval_df = pd.DataFrame(
        {
            "Status": [
                "Approved",
                "Rejected",
                "Pending"
            ],
            "Count": [
                approved,
                rejected,
                pending
            ]
        }
    )

    with gr.Column():

        gr.Markdown(
            """
# 🛡 Enterprise AI Auditor

AI Governance & Compliance Platform
"""
        )

        refresh_button = gr.Button(
            "🔄 Refresh Dashboard"
        )

        # KPI ROW 1
        with gr.Row():

            total_audits_box = gr.Number(
                value=total_audits,
                label="Total Audits"
            )

            high_risk_box = gr.Number(
                value=high_risk,
                label="High Risk Audits"
            )

            pending_box = gr.Number(
                value=pending,
                label="Pending Approvals"
            )

            approval_rate_box = gr.Number(
                value=approval_rate,
                label="Approval Rate %"
            )

        # KPI ROW 2
        with gr.Row():

            average_risk_box = gr.Number(
                value=average_risk,
                label="Average Risk"
            )

            failed_box = gr.Number(
                value=failed_validations,
                label="Failed Validations"
            )

            policies_box = gr.Number(
                value=total_policies,
                label="Total Policies"
            )

        # Charts
        with gr.Row():

            gr.BarPlot(
                value=risk_df,
                x="Risk Level",
                y="Count",
                title="Risk Distribution"
            )

            gr.BarPlot(
                value=approval_df,
                x="Status",
                y="Count",
                title="Approval Status"
            )

        gr.Markdown(
            """
## Recent Activity

• Audit pipeline executed

• Governance dashboard updated

• Human approval workflow active

• Risk analytics generated
"""
        )

        refresh_button.click(

            fn=get_dashboard_data,

            inputs=[],

            outputs=[

                total_audits_box,

                high_risk_box,

                pending_box,

                approval_rate_box,

                average_risk_box,

                failed_box,

                policies_box
            ]
        )