from ArithmeticOperators import ints_diff, ints_prod, ints_sum


def test_sum():
    assert ints_sum(5, 5) == 10
    assert ints_sum(1, 1) == 2
    assert ints_sum(9, 1) == 10
    assert ints_sum(123, 77) == 200
    assert ints_sum(-5, 5) == 0
    assert ints_sum(9, -9) == 0


def test_diff():
    assert ints_diff(5, 5) == 0
    assert ints_diff(5, -5) == 10
    assert ints_diff(12, 7) == 5
    assert ints_diff(5, 0) == 5
    assert ints_diff(1, 5) == -4


def test_prod():
    assert ints_prod(5, 5) == 25
    assert ints_prod(5, 0) == 0
    assert ints_prod(2, 99) == 198
    assert ints_prod(1, 999) == 999
