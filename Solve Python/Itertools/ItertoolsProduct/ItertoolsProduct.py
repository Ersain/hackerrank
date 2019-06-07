'''
Problem: itertools.product()
Description: Given two lists A and B,
Print their Cartesian Product.
Points: 10.

'''


from itertools import product

row1 = input()
row2 = input()

a = row1.split(' ')
b = row2.split(' ')

a = [int(i) for i in a]
b = [int(i) for i in b]

for i in list(product(a, b)):
    print(i, end=" ")
