# stage3/S3_DICT_03.py
def pick(d, keys):
    return {k: d[k] for k in keys if k in d}


# Test
user = {"id": 1, "name": "Alice", "email": "a@b.com"}
print(f"Pick id, name: {pick(user, ['id', 'name'])}")
