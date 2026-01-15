# stage1/S1_MC_01.py


def day_name(n: int):
    match n:
        case 1:
            return "Monday"
        case 2:
            return "Tuesday"
        case 3:
            return "Wednesday"
        case 4:
            return "Thursday"
        case 5:
            return "Friday"
        case 6:
            return "Saturday"
        case 7:
            return "Sunday"
        case _:
            return None


def main():

    test_values = [1, 3, 5, 7, 0, 8]

    print(f"{'Input (n)':<10} | {'Day Name'}")
    print("-" * 25)

    for n in test_values:
        print(f"{n:<10} | {day_name(n)}")


if __name__ == "__main__":
    main()
