# stage3/S3_PIPE_02.py


def compose(*fns):

    def inner(x):
        for f in reversed(fns):
            x = f(x)
        return x

    return inner


def main():
    inc = lambda x: x + 1
    double = lambda x: x * 2

    f_pipe = lambda x: (x + 1) * 2
    f_compose = compose(lambda x: x + 1, lambda x: x * 2)

    print(f"Input: 5")
    print(f"Compose Result: {f_compose(5)}")
    print("-" * 20)
    print("Karşılaştırma:")
    print(f"inc -> double (pipe): {(5+1)*2}")
    print(f"inc -> double (compose): {(5*2)+1}")


if __name__ == "__main__":
    main()
