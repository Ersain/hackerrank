'''
Problem: Loops
Description: Given an integer n, print i^2 for all non-negative integers i < n.
Points: 10.

'''


def squares(n):
    squares_list = [i*i for i in range(n)]
    return '\n'.join(map(str, squares_list))


if __name__ == '__main__':
    n = int(input())

    print(squares(n))
