'''
Problem: Map and Lambda Function.
Description: Given an integer n.
Print the fibonacci sequence until n,
where each member of the sequence is x^3.
E.g.
5 -> [0, 1, 1, 8, 27]

Points: 20.


'''


cube = lambda x: x*x*x


def fibonacci(n):
    fib = [0]*n

    if n > 1:
        fib[1] = 1

        for i in range(2, n):
            fib[i] = fib[i-1]+fib[i-2]

    return fib


def test_cube():
    assert cube(1) == 1
    assert cube(2) == 8


def test_fib_1():
    assert fibonacci(0) == []
    assert fibonacci(1) == [0]


def test_fib_2():
    assert fibonacci(3) == [0, 1, 1]
    assert fibonacci(5) == [0, 1, 1, 2, 3]
