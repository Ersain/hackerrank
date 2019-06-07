'''
Problem: Print Function
Description: Read an integer n and print 123..n.
Points: 20.

'''


if __name__ == '__main__':
    n = int(input())

    for i in range(1, n+1):
        print(i, end='')
