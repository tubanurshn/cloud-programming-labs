# stage3/S3_DICT_02.py


def merge_defaults(defaults, overrides):
    return defaults | overrides


def1 = {"theme": "dark", "notify": {"email": True, "sms": False}}
over1 = {"notify": {"email": False}}

result = merge_defaults(def1, over1)
print(f"Merged: {result}")
