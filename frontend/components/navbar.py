"""
=====================================================
Component : Navbar
Purpose   : Common Navigation
=====================================================
"""

import gradio as gr


# Render navigation bar
# Shared across pages
def navbar():

    with gr.Row():

        gr.Button(
            "Dashboard"
        )

        gr.Button(
            "Upload"
        )

        gr.Button(
            "Reports"
        )

        gr.Button(
            "Governance"
        )

        gr.Button(
            "Logout"
        )