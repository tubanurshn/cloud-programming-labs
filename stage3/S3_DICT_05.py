# stage3/S3_DICT_05.py

def invert(d):
    inverted = {}
    for k, v in d.items():
        if v not in inverted:
            inverted[v] = [k]
        else:
            inverted[v].append(k)
    return inverted

roles = {"Alice": "Admin", "Bob": "User", "Charlie": "Admin"}
print(f"Inverted roles: {invert(roles)}") 