import jwt

SECRET_KEY = "my_super_secret_key"
WRONG_SECRET = "wrong_secret"

payload = {
    "user_id": 1,
    "username": "Sai"
}

token = jwt.encode(
    payload,
    SECRET_KEY,
    algorithm="HS256"
)

try:
    decoded = jwt.decode(
        token,
        WRONG_SECRET,
        algorithms=["HS256"]
    )
    print(decoded)

except jwt.InvalidSignatureError:
    print("Invalid Signature!")