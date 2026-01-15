# stage1/S1_VAR_04.py


def main():

    list_a = [1, 2, 3]
    list_b = [1, 2, 3]

    print(f"list_a: {list_a}")
    print(f"list_b: {list_b}")

    print(f"list_a == list_b: {list_a == list_b}")
    # Result: True (they have the same elements)

    print(f"list_a is list_b: {list_a is list_b}")
    # Result: False (they are different objects in memory )

    x = None
    if x is None:
        print("x is indeed None")

    # Use is for identity, == for equality.


if __name__ == "__main__":
    main()
