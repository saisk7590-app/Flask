import jwt
from datetime import datetime, timedelta
import time

SECRET_KEY = "my_super_secret_key"

payload = {
    "user_id": 1,
    "username": "Sai",
    "exp": datetime.utcnow() + timedelta(seconds=5)
}

token = jwt.encode(
    payload,
    SECRET_KEY,
    algorithm="HS256"
)

print("Token:")
print(token)

print("\nWaiting 6 seconds...")
time.sleep(6)

try:
    decoded = jwt.decode(
        token,
        SECRET_KEY,
        algorithms=["HS256"]
    )
    print(decoded)

except jwt.ExpiredSignatureError:
    print("Token has expired!")