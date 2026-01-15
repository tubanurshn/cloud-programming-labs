# stage1/S1_VAR_05.py


def is_truthy(v):

    return bool(v)


def main():

    test_values = [0, 1, "", "0", [], [0], {}, None]

    print(f"{'Value':<10} | {'Type':<10} | {'Is Truthy?'}")
    print("-" * 35)

    for v in test_values:
        result = is_truthy(v)
        display_val = f'"{v}"' if isinstance(v, str) else str(v)

        print(f"{display_val:<10} | {type(v).__name__:<10} | {result}")


if __name__ == "__main__":
    main()
