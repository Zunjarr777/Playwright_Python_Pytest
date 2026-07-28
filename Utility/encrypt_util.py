import base64


def encrypt_password(password):
    return base64.b64encode(password.encode()).decode()

def decrypt_password(encrypted_pswd):
    return base64.b64decode(encrypted_pswd.encode()).decode()
