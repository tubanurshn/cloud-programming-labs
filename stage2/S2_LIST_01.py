# stage2/S2_LIST_01.py


def clean_numbers(values):
    float_numbers = []

    for item in values:
        try:
            num = float(str(item).strip())

            float_numbers.append(num)
        except (ValueError, TypeError):

            continue

    return float_numbers


def main():

    dirty_data = [" 1 ", "x", "2", "  3.5  ", "abc", None]

    result = clean_numbers(dirty_data)

    print(f"Original List: {dirty_data}")
    print(f"Cleaned List : {result}")


if __name__ == "__main__":
    main()
