'''
Problem: Set .union() Operation.
Description: Usage of set.union() method on sets.
Points: 10.

'''


n = int(input())
n_set = set(map(int, input().split()))
b = int(input())
b_set = set(map(int, input().split()))

print(len(n_set | b_set))
