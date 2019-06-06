'''
Problem: Integers Come In All Sizes.
Description: Given 4 integers a, b, c, d.
Print a^b + c^d.
Points: 10.

'''


def count(num_a, num_b, num_c, num_d):
    return num_a**num_b + num_c**num_d


# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())

# print(count(a, b, c, d))


def test_count_1():
    assert count(1, 1, 1, 1) == 2
    assert count(1, 5, 1, 6) == 2


def test_count_2():
    assert count(2, 2, 2, 2) == 8
    assert count(2, 3, 2, 4) == 24


def test_count_3():
    assert count(3, 3, 3, 3) == 54
    assert count(3, 4, 3, 4) == 162
