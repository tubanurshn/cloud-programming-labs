# stage1/S1_MC_03.py

def calc(a, op, b):
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        return None

    match op:
        case "+":
            return a + b
        case "-":
            return a - b
        case "*":
            return a * b
        case "/":
            if b == 0:
                return None
            return a / b
        case _:
            return None

def main():
    test_cases = [
        (10, "+", 5),  
        (10, "-", 5),  
        (10, "*", 5),   
        (10, "/", 2),   
        (10, "/", 0),  
        ("x", "+", 5),  
        (10, "?", 5)    
    ]

    print(f"{'Operation':<15} | {'Result'}")
    print("-" * 30)

    for a, op, b in test_cases:
        result = calc(a, op, b)
        print(f"{str(a)} {op} {str(b):<5} | {result}")

if __name__ == "__main__":
    main()