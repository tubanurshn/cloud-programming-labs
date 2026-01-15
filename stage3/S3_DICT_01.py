# stage3/S3_DICT_01.py


def get_path(obj, path, fallback=None):
    parts = path.split(".")
    current = obj

    for part in parts:

        if isinstance(current, dict) and part in current:
            current = current[part]
        else:
            return fallback
    return current


data = {"a": {"b": {"c": 42}}}
print(f"Path 'a.b.c': {get_path(data, 'a.b.c', 'N/A')}")
print(f"Path 'a.x.y': {get_path(data, 'a.x.y', 'N/A')}")
