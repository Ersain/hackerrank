'''
Problem: Python If-Else
Description: Given an integer n, define whether it's weird or not:
            If n is odd, print Weird
            If n is even and in the inclusive range of 2 to 5, print Not Weird
            If n is even and in the inclusive range of 6 to 20, print Weird
            If n is even and greater than 20, print Not Weird.
Points: 10.

'''

N = int(input())

cond = (N % 2 == 0)

if not cond:
    print("Weird")
elif cond and (2 <= N <= 5 or 20 < N):
    print("Not Weird")
elif cond and (6 <= N <= 20):
    print("Weird")
