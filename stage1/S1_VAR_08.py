# stage1/S1_VAR_08.py


def main():
    big_int = 10**100

    print(f"Big Integer: {big_int}")
    print(f"Type: {type(big_int).__name__}")

    print(f"Number of digits: {len(str(big_int))}")

    big_float = float(10**100)
    print(f"\nBig Float: {big_float}")
    print(f"Type: {type(big_float).__name__}")

    incremented_int = big_int + 1
    incremented_float = big_float + 1

    print(f"\nInteger (big_int + 1 == big_int): {incremented_int == big_int}"
          )  # False (Hassasiyet tam)
    print(
        f"Float (big_float + 1 == big_float): {incremented_float == big_float}"
    )  # True (Hassasiyet kayboldu!)

    # Integers in Python have arbitrary precision, while floats follow
    # IEEE 754 and lose precision with very large values.
    print(
        "Integers in Python have arbitrary precision, meaning they can grow as large as the available memory allows. In contrast, floats follow the IEEE 754 standard and suffer from precision loss when dealing with extremely large values."
    )


if __name__ == "__main__":
    main()
