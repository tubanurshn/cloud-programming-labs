# stage1/S1_VAR_01.py
import math


def main():
    my_int = 42
    my_float = 3.14
    my_str = "Hello World"
    my_bool = True
    my_none = None
    my_list = [1, 2, 3]
    my_tuple = (1, 2, 3)
    my_dict = {"name": "Tuba", "task": 1}
    my_set = {1, 2, 3}
    my_func = lambda x: x

    print(f"{'Name':<12} | {'Value':<18} | {'type(x)':<25} | {'__name__'}")
    print("-" * 75)

    variables = [("int", my_int), ("float", my_float), ("str", my_str),
                 ("bool", my_bool), ("None", my_none), ("list", my_list),
                 ("tuple", my_tuple), ("dict", my_dict), ("set", my_set),
                 ("function", my_func)]

    for name, val in variables:

        print(
            f"{name:<12} | {str(val):<18} | {str(type(val)):<25} | {type(val).__name__}"
        )


if __name__ == "__main__":
    main()
