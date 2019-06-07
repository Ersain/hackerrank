'''
Problem: Mod Divmod.
Description: Print integer division,
modulo operator and divmod() of two values.
Points: 10.

'''


def int_division(a, b):
    return a//b


def mod_division(a, b):
    return a % b


def int_division_mod_tuple(a, b):
    return divmod(a, b)


if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(int_division(a, b))
    print(mod_division(a, b))
    print(int_division_mod_tuple(a, b))
