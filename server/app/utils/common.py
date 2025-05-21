import bcrypt

import jwt
from datetime import datetime, timedelta, timezone

from app.config.env import ENVSettings

import random
import string


# hash user password
def hash_password(password: str) -> str:
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()


# verify user password
def verify_password(password: str, hashed_password: str) -> bool:
    return bcrypt.checkpw(password.encode(), hashed_password.encode())


# Generate JWT token
def generate_jwt(user_id: str, expires_delta: timedelta = timedelta(hours=1)) -> str:
    expire = datetime.now(timezone.utc) + expires_delta
    payload = {
        "user_id": user_id,
        "exp": expire,
    }
    token = jwt.encode(payload, ENVSettings.JWT_KEY, algorithm="HS256")
    return token


# Verify JWT token
def verify_jwt(token: str) -> dict:
    try:
        payload = jwt.decode(token, ENVSettings.JWT_KEY, algorithms=["HS256"])
        return payload
    except jwt.ExpiredSignatureError:
        raise ValueError("Token has expired")
    except jwt.InvalidTokenError:
        raise ValueError("Invalid token")


# Generate random password
def generate_random_password(
    length: int = 12,
    use_uppercase: bool = True,
    use_lowercase: bool = True,
    use_digits: bool = True,
    use_special: bool = True,
) -> str:
    """
    Generate a random password with the specified rules.

    Args:
        length (int): Length of the password. Default is 12.
        use_uppercase (bool): Include uppercase letters. Default is True.
        use_lowercase (bool): Include lowercase letters. Default is True.
        use_digits (bool): Include digits. Default is True.
        use_special (bool): Include special characters. Default is True.

    Returns:
        str: Randomly generated password.
    """
    if not any([use_uppercase, use_lowercase, use_digits, use_special]):
        raise ValueError("At least one character type must be enabled")

    # Character pools
    uppercase_pool = string.ascii_uppercase if use_uppercase else ""
    lowercase_pool = string.ascii_lowercase if use_lowercase else ""
    digits_pool = string.digits if use_digits else ""
    special_pool = "!@#$%^&*()-_=+[]{}|;:,.<>?/`~" if use_special else ""

    # Combine pools
    all_characters = uppercase_pool + lowercase_pool + digits_pool + special_pool
    if not all_characters:
        raise ValueError("Character pool is empty. Enable at least one character type.")

    # Generate password
    password = [
        random.choice(pool)
        for pool in (uppercase_pool, lowercase_pool, digits_pool, special_pool)
        if pool
    ]
    password += random.choices(all_characters, k=length - len(password))
    random.shuffle(password)

    return "".join(password)


def find_phone_by_id(phones: list, phone_id: str) -> dict:
    for phone in phones:
        if phone["ID"] == phone_id:
            return phone
    raise ValueError(f"Phone number with ID '{phone_id}' wasn't found")
