'''
Problem: Arithmetic Operators
Description: Read 2 integers and print their sum, difference and product.
Points: 10.

'''


def ints_sum(a, b):
    return a+b


def ints_diff(a, b):
    return a-b


def ints_prod(a, b):
    return a*b


if __name__ == '__main__':
    a = int(input())
    b = int(input())

    print(ints_sum(a, b))
    print(ints_diff(a, b))
    print(ints_prod(a, b))
