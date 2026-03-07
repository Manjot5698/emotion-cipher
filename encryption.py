from cryptography.fernet import Fernet
import os

KEY_FILE = "secret.key"

def load_key():
    if os.path.exists(KEY_FILE):
        with open(KEY_FILE, "rb") as f:
            return f.read()
    else:
        key = Fernet.generate_key()
        with open(KEY_FILE, "wb") as f:
            f.write(key)
        return key

key = load_key()
cipher = Fernet(key)

def encrypt_message(message):
    encrypted = cipher.encrypt(message.encode())
    return encrypted.decode()

def decrypt_message(encrypted_message):
    decrypted = cipher.decrypt(encrypted_message.encode())
    return decrypted.decode()


def encrypt_message(message):
    encrypted = cipher.encrypt(message.encode())
    return encrypted.decode()


def decrypt_message(encrypted_message):
    decrypted = cipher.decrypt(encrypted_message.encode())
    return decrypted.decode()