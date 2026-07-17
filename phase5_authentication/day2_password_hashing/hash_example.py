import bcrypt

password = "hello123"

hashed = bcrypt.hashpw(
    password.encode("utf-8"),
    bcrypt.gensalt()
)

print("Stored Hash:")
print(hashed)

print()

print("Correct Password:")

print(
    bcrypt.checkpw(
        password.encode("utf-8"),
        hashed
    )
)

print()

print("Wrong Password:")

print(
    bcrypt.checkpw(
        "hello".encode("utf-8"),
        hashed
    )
)