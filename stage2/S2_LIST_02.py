# stage2/S2_LIST_02.py


def unique(values):

    result = []
    for item in values:

        if item not in result:
            result.append(item)

    return result


def main():
    test_data = [1, 2, 2, 3, 1, 4, "apple", "apple", "orange"]

    deduplicated = unique(test_data)

    print(f"Original: {test_data}")
    print(f"Unique  : {deduplicated}")


if __name__ == "__main__":
    main()
