# stage1/S1_VAR_09.py


# Type hints suggesting both inputs and output should be integers
def add(a: int, b: int) -> int:
    return a + b


def main():
    # Calling with integers works as expected
    print(f"Result with integers (10 + 20): {add(10, 20)}")

    # Calling with strings - Python does NOT stop this
    # It will concatenate the strings instead of mathematical addition
    print(
        f"Result with strings ('Cloud' + 'System'): {add('Cloud', 'System')}")

    # Required comment about type hints:
    print(
        "Type hints are for tooling/readability, not automatic runtime checks."
    )


if __name__ == "__main__":
    main()
