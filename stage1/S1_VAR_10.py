# stage1/S1_VAR_10.py


def inspect(v):
    # Analyzing the value and storing results in a dictionary
    info = {
        "type_name": type(v).__name__,
        "is_none": v is None,
        "is_callable": callable(v),
        "truthy": bool(v)
    }

    # Check if the value can be used in a loop
    try:
        iter(v)
        info["is_iterable"] = True
    except TypeError:
        # If iter(v) raises a TypeError, it's not iterable
        info["is_iterable"] = False

    return info


def main():
    # 10 different values to test
    test_data = [
        10,  # int
        "Hello",  # str
        [1, 2],  # list (iterable)
        (3, 4),  # tuple (iterable)
        None,  # NoneType
        True,  # bool
        {},  # dict (empty, so truthy is False)
        lambda x: x,  # function (callable)
        3.14,  # float
        {1, 2, 3}  # set (iterable)
    ]

    print(f"{'Value':<12} | Inspector Result")
    print("-" * 80)

    for item in test_data:
        # Pretty-printing the results for readability
        result = inspect(item)
        print(f"{str(item):<12} | {result}")


if __name__ == "__main__":
    main()
