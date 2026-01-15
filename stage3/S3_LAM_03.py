# stage3/S3_LAM_03.py


def make_adder(x):
    return lambda y: x + y


add10 = make_adder(10)
add3 = make_adder(3)

print(f"Add10(5): {add10(5)}")  
print(f"Add3(5): {add3(5)}")  
