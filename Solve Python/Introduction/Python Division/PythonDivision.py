'''
Problem: "Python: Division"
Description: Read 2 integers and
print their integer division and float division.
Points: 10.

'''


def int_division(a, b):
    return a//b


def division(a, b):
    return a/b


if __name__ == '__main__':
    n = int(input())
    m = int(input())

    print(int_division(n, m))
    print(division(n, m))
