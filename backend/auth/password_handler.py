"""
=====================================================
Module : Password Handler
Purpose: Password hashing and verification
=====================================================
"""

from passlib.context import CryptContext


# Initialize bcrypt hashing algorithm
# Used to securely hash passwords
pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)


# Convert plain password into hashed password
# Store only hashed values in database
def hash_password(password: str):

    return pwd_context.hash(password)


# Verify user password during login
# Compare entered password with stored hash
def verify_password(
        plain_password: str,
        hashed_password: str
):

    return pwd_context.verify(
        plain_password,
        hashed_password
    )