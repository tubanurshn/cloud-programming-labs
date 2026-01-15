# stage2/S2_FOR_05.py


def print_multiplication_table():
    for row in range(1, 11):
        for col in range(1, 11):
            product = row * col
            print(f"{product:>4}", end="")

        print()


def main():
    print("--- 10x10 Multiplication Table ---")
    print_multiplication_table()


if __name__ == "__main__":
    main()
