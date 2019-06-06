'''
Problem: Power - Mod Power.
Description: Given integers a, b, c -
print (a^b) and (a^b % c).
Points: 10.

'''


def count_pow(a, b):
    return pow(a, b)


def count_pow_mod(a, b, c):
    return pow(a, b, c)


# a = int(input())
# b = int(input())
# c = int(input())
# print(pow(a, b))
# print(pow(a, b, c))


def test_count_pow():
    assert count_pow(3, 3) == 27
    assert count_pow(2, 10) == 1024


def test_count_pow_mod():
    assert count_pow_mod(3, 3, 2) == 1
    assert count_pow_mod(2, 10, 5) == 4


def test_count():
    assert count_pow(3, 2) > count_pow_mod(3, 2, 2)
    assert count_pow(7, 3) > count_pow_mod(7, 3, 10)
