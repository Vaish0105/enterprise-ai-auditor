"""
=====================================================
Component : Role Router
Purpose   : Route user to dashboard
=====================================================
"""


# Determine dashboard
# Based on role
def get_dashboard(role):

    # Admin dashboard
    # Full system access
    if role == "admin":

        return "admin"

    # Auditor dashboard
    # Audit operations access
    elif role == "auditor":

        return "auditor"

    # Employee dashboard
    # Claim submission access
    else:

        return "employee"