'''
Problem: Print Function
Description: Read an integer n and print 123..n.
Points: 20.

'''


def until_n(n):
    return int(''.join([str(i) for i in range(1, n+1)]))


if __name__ == '__main__':
    a = int(input())

    print(until_n(a))
