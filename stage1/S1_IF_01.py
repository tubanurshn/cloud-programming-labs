# stage1/S1_IF_01.py


def shipping_cost(weight_kg, is_member):
    # If it is not integer or float or less than 0, return None
    if not isinstance(weight_kg, (int, float)) or weight_kg <= 0:
        return None

    if weight_kg <= 1:
        cost = 10
    elif weight_kg <= 5:
        cost = 20
    else:
        cost = 30

    if is_member:
        cost = cost * 0.8  # %20 discount

    return cost


def main():
    test_cases = [(0.5, False), (1, False), (3, False), (5, True), (10, False),
                  (-2, False), ("abc", False)]

    print(f"{'Weight':<10} | {'Member':<8} | {'Result'}")
    print("-" * 35)

    for weight, member in test_cases:
        result = shipping_cost(weight, member)
        print(f"{str(weight):<10} | {str(member):<8} | {result}")


if __name__ == "__main__":
    main()
