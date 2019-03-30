from itertools import product

# Enter your code here. Read input from STDIN. Print output to STDOUT
row1 = input()
row2 = input()

A = row1.split(' ')
B = row2.split(' ')

A = [int(i) for i in A]
B = [int(i) for i in B]

for i in list(product(A, B)):
    print(i, end = " ")
