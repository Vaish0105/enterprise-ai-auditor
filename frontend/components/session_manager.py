"""
=====================================================
Component : Session Manager
=====================================================
"""


# Global session storage
# Temporary MVP solution
CURRENT_USER = {}


# Save logged-in user
# Store role and token
def set_session(data):

    global CURRENT_USER

    CURRENT_USER = data


# Retrieve session
# Used by dashboards
def get_session():

    return CURRENT_USER


# Logout user
# Clear memory
def clear_session():

    global CURRENT_USER

    CURRENT_USER = {}