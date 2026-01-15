# stage2/S2_FOR_04.py


def count_occurrences(values):
    counts = {}

    for item in values:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1

    return counts


def main():
    test_cases = [["apple", "banana", "apple", "cherry", "banana", "apple"],
                  [1, 2, 2, 3, 3, 3, 4, 4, 4, 4], ["A", "B", "A", "C", "A"],
                  []]

    for case in test_cases:
        result = count_occurrences(case)
        print(f"Input: {case}")
        print(f"Counts: {result}\n")


if __name__ == "__main__":
    main()
