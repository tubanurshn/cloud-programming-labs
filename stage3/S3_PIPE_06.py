# stage3/S3_PIPE_06.py


def pipe_safe(*fns):

    def inner(x):
        try:
            for f in fns:
                x = f(x)
            return {"ok": True, "value": x}
        except Exception as e:
            return {"ok": False, "error": str(e)}

    return inner


risky_div = lambda x: 10 / x
safe_calc = pipe_safe(risky_div, lambda x: x + 1)

print(f"Success: {safe_calc(2)}")
print(f"Failure: {safe_calc(0)}")
