'''
Problem: Exceptions.
Description: Given 2 numbers a and b,
try to print a//b.
Points: 10.

'''


for i in range(int(input())):
    try:
        a, b = map(int, input().split())
        print(a//b)
    except (ZeroDivisionError, ValueError) as e:
        print("Error Code:", e)
