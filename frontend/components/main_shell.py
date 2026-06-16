"""
=====================================================
Component : Main Shell
Purpose : Enterprise Application Layout
=====================================================
"""

import gradio as gr

from frontend.pages.dashboard import (
    build_dashboard
)

from frontend.pages.audit_details import (
    build_audit_details_page
)

from frontend.pages.audit_search import (
    build_audit_search_page
)

from frontend.pages.upload import (
    build_upload_page
)

from frontend.pages.audits import (
    build_audit_workspace
)

from frontend.pages.reports import (
    build_reports_page
)

from frontend.pages.audit_history import (
    build_audit_history
)

from frontend.pages.approval_dashboard import (
    build_approval_dashboard
)

from frontend.pages.governance import (
    build_governance_page
)


# Build main application shell
# Enterprise tab layout
def build_main_shell():

    with gr.Blocks(

    title="Enterprise AI Auditor",

    theme=gr.themes.Soft(),

    css="""
    .gradio-container {
        max-width: 1600px !important;
    }

    h1 {
        color: #1f4e79;
    }

    h2 {
        color: #2f6fad;
    }
    """
) as shell:

        # Dashboard tab
        with gr.Tab(
            "Dashboard"
        ):
            build_dashboard()

        # Upload tab
        with gr.Tab(
            "Upload"
        ):
            build_upload_page()

        # Audit Workspace
        with gr.Tab(
            "Audits"
        ):
            build_audit_workspace()

        # Audit Search  
        with gr.Tab("Audit Search"):

            build_audit_search_page()

        # Reports
        with gr.Tab(
            "Reports"
        ):
            build_reports_page()

        # Audit History
        with gr.Tab(
            "Audit History"
        ):
            build_audit_history()

        with gr.Tab("Audit Details"):

            build_audit_details_page()

        # Approval Dashboard
        with gr.Tab(
            "Approvals"
        ):
            build_approval_dashboard()

        # Governance
        with gr.Tab(
            "Governance"
        ):
            build_governance_page()

    return shell