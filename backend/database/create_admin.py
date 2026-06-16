"""
=====================================================
Module : Create Admin User
Purpose: Generate hashed password
=====================================================
"""

from backend.auth.password_handler import hash_password


# Generate hash for default admin password
# Use this value in PostgreSQL
hashed_password = hash_password(
    "Admin@123"
)

print(hashed_password)