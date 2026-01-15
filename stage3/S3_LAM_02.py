# stage3/S3_LAM_02.py

people = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 20},
    {"name": "Charlie", "age": 25}
]

sorted_people = sorted(people, key=lambda p: p["age"])

print("Before:", people)
print("After (Sorted by Age):", sorted_people)