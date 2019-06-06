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


# a = int(input())
# b = int(input())
# print(int_division(a, b))
# print(mod_division(a, b))
# print(int_division_mod_tuple(a, b))


def test_div():
    assert int_division(5, 6) == 0
    assert int_division(13, 5) == 2


def test_mod():
    assert mod_division(5, 2) == 1
    assert mod_division(20, 3) == 2


def test_divmod():
    assert int_division_mod_tuple(7, 3) == (2, 1)
    assert int_division_mod_tuple(29, 21) == (1, 8)
