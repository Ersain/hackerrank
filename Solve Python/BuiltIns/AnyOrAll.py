'''
Problem: Any or All.
Description: Given a list of integers,
If all the integers are positive,
then check if any integer is a palindromic integer..
Points: 20.

'''


def check(arr):
    return all(int(i) > 0 for i in arr) and any(i == i[::-1] for i in arr)


# N = int(input())
# integers = input().split()
# print(check(integers))


def test_check_1():
    assert check(['12', '9', '61', '5', '14']) is True


def test_check_2():
    assert check(['1', '2', '3', '4', '5', '-9']) is False


def test_check_3():
    assert check([0]) is False
