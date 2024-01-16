import os
from cryptography.fernet import Fernet


def encrypt(data):
    fernet = Fernet(os.getenv("key_fernet").encode())
    return fernet.encrypt(data.encode()).decode()


def dcrypt(data):
    fernet = Fernet(os.getenv("key_fernet").encode())
    return fernet.decrypt(data).decode()
