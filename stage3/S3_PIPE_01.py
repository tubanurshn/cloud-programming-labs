# stage3/S3_PIPE_01.py


def pipe(*fns):

    def inner(x):
        for f in fns:
            x = f(x)
        return x

    return inner


def main():
    inc = lambda x: x + 1
    double = lambda x: x * 2
    square = lambda x: x**2

    pipeline = pipe(inc, double, square)

    print(f"Result (pipe): {pipeline(5)}")


if __name__ == "__main__":
    main()
