#!/usr/bin/env python3
"""
Ultra-secure password generator
Generates 24-character passwords with:
- Upper/lowercase letters
- Digits
- Special characters
"""
import secrets
import string

def generate() -> str:
    """Generate one 24-char password"""
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    while True:
        password = ''.join(secrets.choice(chars) for _ in range(24))
        # Ensure at least one of each char type
        if (any(c.islower() for c in password)
                and any(c.isupper() for c in password)
                and any(c.isdigit() for c in password)
                and any(c in "!@#$%^&*" for c in password)):
            return password


print(generate())