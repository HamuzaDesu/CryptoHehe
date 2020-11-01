from cryptography.fernet import Fernet

key = 0
token = 0

with open('key.txt', 'rb') as f:
    key = f.readline()
with open('token.txt', 'rb') as f:
    token = f.readline()


f = Fernet(key)

decryption = f.decrypt(token)

print(f'Result: {decryption}')