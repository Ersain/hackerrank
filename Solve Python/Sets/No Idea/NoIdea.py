'''
Problem: No Idea!
Description: Given a list of integers
and 2 disjoint sets A and B.
You have initial happiness = 0.
For each integer i,
where i in A, your happiness increments,
and if i in B, decrements.
Print you final happiness.
Points: 50.

'''


happiness = 0
n, m = map(int, input().split())
arr = list(map(int, input().split()))
set_a = set(map(int, input().split()))
set_b = set(map(int, input().split()))

for i in arr:
    if i in set_a:
        happiness += 1
    elif i in set_b:
        happiness -= 1

print(happiness)
