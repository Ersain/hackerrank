'''
Problem: Set .intersection() Operation.
Description: Usage of set.intersection() method on sets.

'''


n = int(input())
n_set = set(map(int, input().split()))
b = int(input())
b_set = set(map(int, input().split()))

print(len(n_set & b_set))
