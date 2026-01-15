# stage3/S3_DICT_04.py
def omit(d, keys):
    return {k: v for k, v in d.items() if k not in keys}


user = {"id": 1, "name": "Alice", "email": "a@b.com"}
print(f"Omit email: {omit(user, ['email'])}")