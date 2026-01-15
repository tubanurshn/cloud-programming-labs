# stage1/S1_IF_03.py


def normalize_name(x):
    # If x is None return "Anonymous"
    if not x:
        return "Anonymous"

    stripped_name = str(x).strip()  #delete spaces from both sides

    if stripped_name == "":
        return "Anonymous"

    return stripped_name


def main():
    test_cases = ["", " ", None, " Ola "]

    print(f"{'Input':<12} | {'Result'}")
    print("-" * 30)

    for case in test_cases:

        display_input = repr(case)
        result = normalize_name(case)
        print(f"{display_input:<12} | {result}")


if __name__ == "__main__":
    main()
