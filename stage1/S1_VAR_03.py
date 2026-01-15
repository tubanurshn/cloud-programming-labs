# stage1/S1_VAR_03.py


def main():
    lst = [1, 2, 3]
    lst[0] = 100
    print(f"Modified list: {lst}")

    tup = (1, 2, 3)
    print(f"Original tuple: {tup}")

    try:
        tup[0] = 100
    except TypeError as e:
        print(f"Caught exception: {e}")

    # Explanation: Lists are mutable, meaning their contents can be modified after creation.
    # Tuples are immutable, so their elements cannot be changed once defined.


if __name__ == "__main__":
    main()
