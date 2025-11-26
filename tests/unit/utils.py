# utils.py

import os
import json
import jwt
import hashlib
from datetime import datetime, timedelta
from user_dashboard.settings import SECRET_KEY

def get_current_datetime():
    """Returns the current datetime object."""
    return datetime.now()

def generate_password_hash(password):
    """Generates a SHA256 hash of the provided password."""
    return hashlib.sha256(password.encode('utf-8')).hexdigest()

def validate_password(password, password_hash):
    """Checks if the provided password matches the given hash."""
    return generate_password_hash(password) == password_hash

def generate_jwt_token(user_id, expires_in=3600):
    """Generates a JWT token with the provided user ID and expiration time."""
    payload = {
        'user_id': user_id,
        'exp': datetime.utcnow() + timedelta(seconds=expires_in)
    }
    return jwt.encode(payload, SECRET_KEY, algorithm='HS256')

def validate_jwt_token(token):
    """Verifies the provided JWT token."""
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        return payload
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None

def load_json_file(file_path):
    """Loads a JSON file and returns its contents."""
    with open(file_path, 'r') as file:
        return json.load(file)

def save_json_file(file_path, data):
    """Saves the provided data to a JSON file."""
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)