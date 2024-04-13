import secrets
import hashlib

service = "example.com"
username = "user123"


def generate_password(length=12):
    # Generate a random password with the specified length
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_-+=[]{}<>,."
    password = ''.join(secrets.choice(alphabet) for _ in range(length))

    return password


def hash_password(password):
    # Hash the password using the SHA-256 algorithm
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    return hashed_password


def generate():
    # Generate a new password
    new_password = generate_password()
    hashed_password = hash_password(new_password)

    return new_password, hashed_password

print(generate_password(10))