'''
Problem: Power - Mod Power.
Description: Given integers a, b, c -
print (a^b) and (a^b % c).
Points: 10.

'''


def count_pow(a, b):
    return pow(a, b)


def count_pow_mod(a, b, c):
    return pow(a, b, c)


a = int(input())
b = int(input())
c = int(input())
print(pow(a, b))
print(pow(a, b, c))
