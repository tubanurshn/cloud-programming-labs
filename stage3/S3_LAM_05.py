# stage3/S3_LAM_05.py


def at_least(min_value):
    return lambda x: x >= min_value


nums = [10, 5, 20, 3, 15]
is_at_least_12 = at_least(12)
result = list(filter(is_at_least_12, nums))

print(f"Numbers >= 12: {result}")
