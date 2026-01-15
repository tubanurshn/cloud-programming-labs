# stage2/S2_LIST_05.py

def stats(nums):
    # If list is empty or not a list, return None
    if not nums or not isinstance(nums, list):
        return None

    total_sum = sum(nums)
    average = total_sum / len(nums)
    minimum = min(nums)
    maximum = max(nums)

    #dictionary
    return {
        "min": minimum,
        "max": maximum,
        "avg": average,
        "sum": total_sum
    }

def main():
    test_cases = [
        [10, 20, 30, 40, 50],          
        [-10, -5, 0, 5, 10],          
        [-100, -200, -50],            
        [3.14, 1.59, 2.65],            
        []                            
    ]

    print(f"{'Input List':<25} | {'Stats Result'}")
    print("-" * 75)

    for case in test_cases:
        result = stats(case)
        print(f"{str(case):<25} | {result}")

if __name__ == "__main__":
    main()