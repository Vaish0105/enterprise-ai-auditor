"""
=====================================================
Component : Dashboard Renderer
Purpose   : Render Role Dashboard
=====================================================
"""

from frontend.pages.admin_dashboard import (
    admin_dashboard
)


# Display dashboard
# Based on user role
def render_dashboard(role):

    # Admin dashboard
    # Full access view
    if role == "admin":

        admin_dashboard()

    # Auditor dashboard
    # Will be implemented next
    elif role == "auditor":

        pass

    # Employee dashboard
    # Will be implemented next
    else:

        pass