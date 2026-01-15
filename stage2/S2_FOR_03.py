# stage2/S2_FOR_03.py


def sum_until(nums, threshold):
    current_sum = 0

    for n in nums:
        if current_sum + n > threshold:
            break

        current_sum += n

    return current_sum


def main():
    test_cases = [([10, 20, 30, 40], 55), ([1, 2, 3, 4, 5], 10),
                  ([100, 200], 50), ([5, 5, 5], 20), ([], 10)]

    print(f"{'Numbers':<20} | {'Threshold':<10} | {'Final Sum'}")
    print("-" * 45)

    for nums, thres in test_cases:
        result = sum_until(nums, thres)
        print(f"{str(nums):<20} | {thres:<10} | {result}")


if __name__ == "__main__":
    main()
