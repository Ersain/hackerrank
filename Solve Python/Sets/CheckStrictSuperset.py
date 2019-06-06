'''
Problem: Check Strict Superset.
Description: Check if a given set A is a super set of
the following N sets.
Points: 10.

'''


a = set(map(str, input().split(' ')))
strict_set = []

for i in range(int(input())):
    cond = set(map(str, input().split(' ')))
    strict_set.append(a.issuperset(cond))

print(all(strict_set))
