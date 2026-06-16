"""
=====================================================
Module : User Repository
Purpose: Fetch users from PostgreSQL
=====================================================
"""

from sqlalchemy import text

# Import SQLAlchemy engine
# Used for database connections
from backend.database.postgres import engine


# Get user using email address
# Returns matching database row
def get_user_by_email(email):

    # Open database connection
    # Auto closes after execution
    with engine.connect() as conn:

        # Execute SQL query
        # Search user by email
        result = conn.execute(
            text(
                """
                SELECT *
                FROM users
                WHERE email = :email
                """
            ),
            {"email": email}
        )

        # Return first matching user
        # Returns None if not found
        return result.fetchone()