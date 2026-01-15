# stage3/S3_PIPE_03.py


def pipe(*fns):

    def inner(x):
        for f in fns:
            x = f(x)
        return x

    return inner


def normalize_string(text):
    strip_f = lambda s: s.strip()
    lower_f = lambda s: s.lower()
    collapse_f = lambda s: " ".join(s.split())

    pipeline = pipe(strip_f, lower_f, collapse_f)
    return pipeline(text)


def main():
    test_input = "  Ala    Ma    Kota  "
    print(f"Original  : '{test_input}'")
    print(f"Normalized: '{normalize_string(test_input)}'")


if __name__ == "__main__":
    main()
