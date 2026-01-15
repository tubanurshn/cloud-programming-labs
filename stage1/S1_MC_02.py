# stage1/S1_MC_02.py


def run_command(cmd):
    match cmd:
        case "start":
            return "System is starting..."
        case "stop":
            return "System is shutting down..."
        case "status":
            return "System is healthy."
        case _:
            return "UNKNOWN_COMMAND"


def main():
    commands = ["start", "status", "stop", "exit", "restart"]

    print(f"{'Command':<10} | {'Result'}")
    print("-" * 35)

    for c in commands:
        result = run_command(c)
        print(f"{str(c):<10} | {result}")


if __name__ == "__main__":
    main()
