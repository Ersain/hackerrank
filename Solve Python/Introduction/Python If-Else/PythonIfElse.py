'''
Problem: Python If-Else
Description: Given an integer n, define whether it's weird or not:
            If n is odd, print Weird
            If n is even and in the inclusive range of 2 to 5, print Not Weird
            If n is even and in the inclusive range of 6 to 20, print Weird
            If n is even and greater than 20, print Not Weird.
Points: 10.

'''


def is_weird(n):
    cond = (n % 2 == 0)

    if not cond:
        return ("Weird")
    elif cond and (2 <= n <= 5 or 20 < n):
        return ("Not Weird")
    elif cond and (6 <= n <= 20):
        return ("Weird")


if __name__ == "__main__":
    N = int(input())
    print(is_weird(N))
