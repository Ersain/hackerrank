from fractions import Fraction
from ReduceFunction import product


def test_product_1():
    fracs = [Fraction(1, 2), Fraction(3, 4), Fraction(5, 3)]
    assert product(fracs) == (5, 8)


def test_product_2():
    fracs = [Fraction(1, 2), Fraction(1, 2)]
    assert product(fracs) == (1, 4)


def test_product_3():
    fracs = [Fraction(1, 2), Fraction(5, 6), Fraction(1, 2), Fraction(3, 2)]
    assert product(fracs) == (5, 16)
