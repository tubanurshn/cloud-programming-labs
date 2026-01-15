# stage2/S2_FOR_01.py


def fizzbuzz(n):
    # range(1, n+1) includes 1 to n
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)


def main():
    print("--- FizzBuzz (1 to 30) ---")
    fizzbuzz(30)


if __name__ == "__main__":
    main()
