#!/usr/bin/env python3
"""generate hashed password using werkzeug"""
from werkzeug.security import generate_password_hash
# import os

def hash_password_generator():
    input_env_variable_name = input("Enter the env variable name: ")
    env_variable_name = input_env_variable_name.upper()
    password = input("Enter the password: ")

    hashed_password = generate_password_hash(password, method='pbkdf2:sha256', salt_length=16)
    with open(".env", "a") as f:
        f.write(f"{env_variable_name}={hashed_password}")

if __name__ == "__main__":
    hash_password_generator()
