import jwt

SECRET_KEY = "my_super_secret_key"

payload = {
    "user_id": 1,
    "username": "Sai"
}

token = jwt.encode(
    payload,
    SECRET_KEY,
    algorithm="HS256"
)

decoded = jwt.decode(
    token,
    SECRET_KEY,
    algorithms=["HS256"]
)

print("Decoded Payload:")
print(decoded)