# stage2/S2_LIST_04.py


def flatten1(lst):
    # make it one full list by seperating the sublists
    flat_list = []

    for item in lst:

        if isinstance(item, list):
            for sub_item in item:
                flat_list.append(sub_item)
        else:
            flat_list.append(item)

    return flat_list


def main():

    nested_data = [1, [2, 3], 4, [5, 6, 7], "apple", ["orange"]]

    result = flatten1(nested_data)

    print(f"Original: {nested_data}")
    print(f"Flattened: {result}")


if __name__ == "__main__":
    main()
