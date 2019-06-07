'''
Problem: Python Evaluation.
Description: Given a math expression,
print the result of it.
Points: 20.

'''


def solve(string):
    return eval(string)

# eval(input())


def test_solve_1():
    assert solve("9 + 5") == 14


def test_solve_2():
    assert solve("abs(complex(6, 8))") == 10


def test_solve_3():
    assert solve("1024>>9") == 2
