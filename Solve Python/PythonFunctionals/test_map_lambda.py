from MapAndLambda import cube, fibonacci


def test_cube():
    assert cube(1) == 1
    assert cube(2) == 8


def test_fib_1():
    assert fibonacci(0) == []
    assert fibonacci(1) == [0]


def test_fib_2():
    assert fibonacci(3) == [0, 1, 1]
    assert fibonacci(5) == [0, 1, 1, 2, 3]
