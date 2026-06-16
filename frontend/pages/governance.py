"""
=====================================================
Page : Governance Dashboard
Purpose : AI Governance Metrics
=====================================================
"""

import pandas as pd
import gradio as gr

from backend.database.dashboard_repository import (

    get_average_risk,

    get_high_risk_audits,

    get_pending_approvals,

    get_approval_rate,

    get_risk_distribution
)


def build_governance_page():

    average_risk = get_average_risk()

    high_risk = get_high_risk_audits()

    pending = get_pending_approvals()

    approval_rate = get_approval_rate()

    risk_data = get_risk_distribution()

    chart_df = pd.DataFrame(
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

    with gr.Column():

        gr.Markdown(
            "# 🛡 Governance Dashboard"
        )

        with gr.Row():

            gr.Number(
                value=high_risk,
                label="High Risk Audits"
            )

            gr.Number(
                value=pending,
                label="Pending Approvals"
            )

        with gr.Row():

            gr.Number(
                value=approval_rate,
                label="Approval Rate %"
            )

            gr.Number(
                value=average_risk,
                label="Average Risk Score"
            )

        gr.Markdown(
            "## 📊 Risk Distribution"
        )

        gr.BarPlot(
            value=chart_df,
            x="Risk Level",
            y="Count",
            title="Audit Risk Distribution"
        )

        if approval_rate >= 80:

            health = "🟢 Healthy"

        elif approval_rate >= 50:

            health = "🟡 Attention Required"

        else:

            health = "🔴 Governance Risk"

        gr.Markdown(
            f"""
## Governance Health

{health}
"""
        )