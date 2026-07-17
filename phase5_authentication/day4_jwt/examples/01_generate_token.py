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

print("Generated Token:")
print(token)