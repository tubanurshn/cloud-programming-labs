# stage2/S2_FOR_02.py


def find_first_even(nums):
    if not isinstance(nums, list) or not nums:
        return None

    for n in nums:
        if n % 2 == 0:
            return n
    return None


def main():
    test_cases = [
        [1, 3, 5, 8, 10],  
        [1, 3, 5, 7],  
        [2, 4, 6], 
        [], 
        [11, -4, 7]  
    ]

    print(f"{'Input List':<20} | {'First Even'}")
    print("-" * 35)

    for case in test_cases:
        result = find_first_even(case)
        print(f"{str(case):<20} | {result}")


if __name__ == "__main__":
    main()
