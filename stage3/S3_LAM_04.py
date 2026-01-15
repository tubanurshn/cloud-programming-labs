# stage3/S3_LAM_04.py

nums = [1, 2, 3, 4, 5, 6]

evens = list(filter(lambda x: x % 2 == 0, nums))

squares = list(map(lambda x: x**2, evens))

total = sum(squares)

print(f"Initial: {nums}")
print(f"Filtered (Evens): {evens}")
print(f"Mapped (Squares): {squares}")
print(f"Final Sum: {total}")
