# stage3/S3_LAM_06.py


def map_values(d, fn):
    return {k: fn(v) for k, v in d.items()}


prices = {"apple": 10, "banana": 20}
inflation_prices = map_values(prices, lambda v: v * 1.5)

print(f"Original: {prices}")
print(f"After 50% increase: {inflation_prices}")
