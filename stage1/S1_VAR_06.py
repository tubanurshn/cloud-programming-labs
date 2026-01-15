# stage1/S1_VAR_06.py


def to_int_or_none(s):
    try:
        return int(s)
    except (ValueError, TypeError):
        return None


def main():
    test_cases = ["12", " 12 ", "12x", "", None]

    print(f"{'Input':<10} | {'Result':<10} | {'Type'}")
    print("-" * 35)

    for case in test_cases:
        result = to_int_or_none(case)
        display_input = f'"{case}"' if isinstance(case, str) else str(case)
        result_type = type(result).__name__

        print(f"{display_input:<10} | {str(result):<10} | {result_type}")


if __name__ == "__main__":
    main()
