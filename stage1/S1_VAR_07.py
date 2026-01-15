# stage1/S1_VAR_07.py
import math


def main():
    nan1 = float("nan")

    try:
        nan2 = 0.0 / 0.0
    except ZeroDivisionError:
        nan2 = float("nan")

    print("--- NaN Comparisons ---")
    #never equals
    print(f"nan1 == nan1: {nan1 == nan1}")
    print(f"nan1 == nan2: {nan1 == nan2}")

    print("\n--- Detection using math.isnan ---")
    print(f"math.isnan(nan1): {math.isnan(nan1)}")
    print(f"math.isnan(nan2): {math.isnan(nan2)}")

    print(f"math.isnan(42.0): {math.isnan(42.0)}")


if __name__ == "__main__":
    main()
