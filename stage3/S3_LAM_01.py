# stage3/S3_LAM_01.py

square = lambda n: n ** 2
is_odd = lambda n: n % 2 != 0
greet = lambda name: f"Hello, {name}!"

def main():
    print(f"Square: 4 -> {square(4)}, -3 -> {square(-3)}, 0 -> {square(0)}")

    print(f"Is Odd: 5 -> {is_odd(5)}, 8 -> {is_odd(8)}, -1 -> {is_odd(-1)}")

    print(f"Greet: 'Ali' -> {greet('Ali')}, 'Ece' -> {greet('Ece')}, '' -> {greet('')}")

if __name__ == "__main__":
    main()