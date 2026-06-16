"""
=====================================================
Module : Main Application
Purpose : Launch Enterprise Shell
=====================================================
"""

from frontend.components.main_shell import (
    build_main_shell
)

# Build enterprise shell
# Create application layout
app = build_main_shell()

# Launch application
# Open in browser
app.launch(
    server_name="127.0.0.1",
    server_port=7860,
    inbrowser=True
)