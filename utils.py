import string
import secrets

def generate_passphrase(length=20):
    characters = string.ascii_letters + string.digits + string.punctuation
    pass_phrase = ''.join(secrets.choice(characters) for _ in range(length))
    return pass_phrase

