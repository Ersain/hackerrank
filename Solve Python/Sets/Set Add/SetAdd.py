'''
Problem: Set .add().
Description: Usage of set.add() method.
Points: 10.

'''


n = int(input())
a_set = set()
for i in range(n):
    a_set.add(input())
print(len(a_set))
