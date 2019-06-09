'''
Problem: Reduce Function.
Description: Given a list of rational numbers, find there product.
Points: 30.

'''


from fractions import Fraction
from functools import reduce


def product(fracs):
    t = Fraction(reduce(lambda x, y: x*y, fracs))
    return t.numerator, t.denominator


if __name__ == '__main__':
    fracs = []
    for _ in range(int(input())):
        fracs.append(Fraction(*map(int, input().split())))
    result = product(fracs)
    print(*result)
