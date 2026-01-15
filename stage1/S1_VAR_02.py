# stage1/S1_VAR_02.py


def main():
    x = 42
    print(f"Value: {x:<20} | Type: {type(x).__name__}")

    x = "Hello Python"
    print(f"Value: {x:<20} | Type: {type(x).__name__}")

    x = [1, 2, 3]
    print(f"Value: {str(x):<20} | Type: {type(x).__name__}")

    x = True
    print(f"Value: {str(x):<20} | Type: {type(x).__name__}")

    # Dynamic typing means that the type of a variable is determined at runtime,
    # and the same variable name can be reassigned to values of different types.


if __name__ == "__main__":
    main()
