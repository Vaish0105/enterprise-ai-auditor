"""
=====================================================
Module : Login Screen
Purpose: User Authentication UI
=====================================================
"""

import gradio as gr

from backend.auth.auth_service import (
    authenticate_user
)

# Import session manager
# Store logged-in user information
from frontend.components.session_manager import (
    set_session
)

# Role router
# Determine dashboard
from frontend.components.role_router import (
    get_dashboard
)

# Handle login button click
# Validate credentials
def login_user(
        email,
        password
):

    # Authenticate user
    # Check database records
    result = authenticate_user(
        email,
        password
    )

    # Invalid credentials
    # Display error
    if result is None:
        return " Invalid Credentials"

    # Successful login
    # Show role information
    set_session(result)

    # Determine dashboard
    # Based on role
    dashboard = get_dashboard(
        result["role"]
    )

    # Display welcome message
    # Show user name and role
    return (
    f" Login Successful\n\n"
    f"Role : {result['role']}"
)

# Build login interface
# First screen user sees
with gr.Blocks() as login_ui:

    # Page title
    # Display application name
    gr.Markdown(
        "# Enterprise AI Auditor"
    )

    # Email input field
    # User enters registered email
    email = gr.Textbox(
        label="Email"
    )

    # Password input field
    # Hidden characters
    password = gr.Textbox(
        label="Password",
        type="password"
    )

    # Login button
    # Trigger authentication
    login_button = gr.Button(
        "Login"
    )

    # Output message
    # Show login result
    output = gr.Textbox(
        label="Status"
    )

    # Connect button event
    # Call login function
    login_button.click(
        login_user,
        inputs=[
            email,
            password
        ],
        outputs=output
    )