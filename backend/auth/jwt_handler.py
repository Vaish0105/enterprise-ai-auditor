"""
=====================================================
Module : JWT Handler
Purpose: Create and verify JWT tokens
=====================================================
"""

from jose import jwt

# Import date utilities
# Used for token expiration
from datetime import datetime, timedelta


# Secret key for signing JWT
# Later move this to .env
SECRET_KEY = "AI_AUDITOR_SECRET_KEY"


# JWT algorithm
# Industry standard
ALGORITHM = "HS256"


# Token expiry duration
# User must login again after expiry
ACCESS_TOKEN_EXPIRE_MINUTES = 60


# Generate JWT token
# Returns encoded access token
def create_access_token(data):

    # Create copy of payload
    # Prevent modifying original object
    payload = data.copy()

    # Calculate token expiration
    # Current time + 60 minutes
    expire = (
        datetime.utcnow()
        + timedelta(
            minutes=ACCESS_TOKEN_EXPIRE_MINUTES
        )
    )

    # Add expiry information
    # JWT validates automatically
    payload["exp"] = expire

    # Encode token
    # Return signed JWT string
    return jwt.encode(
        payload,
        SECRET_KEY,
        algorithm=ALGORITHM
    )