'''
Problem: Check Subset.
Description: Check if a given set A is a subset of a set B.

'''


for i in range(int(input())):
    len_a = int(input())
    a_set = set(map(int, input().split()))
    len_b = int(input())
    b_set = set(map(int, input().split()))
    print(a_set.issubset(b_set))
