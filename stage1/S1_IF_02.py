# stage1/S1_IF_02.py


def grade(score):

    if not isinstance(score, (int, float)) or score < 0 or score > 100:
        return None

    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


def main():
    test_scores = [59, 60, 69, 70, 89, 90, 100, 101]

    print(f"{'Score':<10} | {'Grade'}")
    print("-" * 20)

    for s in test_scores:
        result = grade(s)
        print(f"{s:<10} | {result}")


if __name__ == "__main__":
    main()
