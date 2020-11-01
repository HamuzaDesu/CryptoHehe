from cryptography.fernet import Fernet

key = Fernet.generate_key()

f = Fernet(key)

token = f.encrypt(b'at')

with open('key.txt', 'wb') as f:
    f.write(key)
with open('token.txt', 'wb') as f:
    f.write(token)

