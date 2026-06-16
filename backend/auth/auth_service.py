"""
=====================================================
Module : Authentication Service
Purpose: Validate user login
=====================================================
"""

from backend.auth.password_handler import verify_password

from backend.auth.jwt_handler import create_access_token

from backend.database.user_repository import (
    get_user_by_email
)


# Authenticate user
# Returns token and role
def authenticate_user(
        email,
        password
):

    # Fetch user from database
    # Search using email
    db_user = get_user_by_email(
        email
    )

    # Check if user exists
    # Reject unknown users
    if not db_user:

        return None

    # Verify entered password
    # Compare with stored hash
    if not verify_password(
        password,
        db_user.password_hash
    ):

        return None

    # Generate JWT token
    # Store email and role
    token = create_access_token(
        {
            "email": email,
            "role": db_user.role
        }
    )

    return {

        "token": token,

        "role": db_user.role,

        "name": db_user.name
    }