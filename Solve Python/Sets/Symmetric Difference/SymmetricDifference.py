'''
Problem: Symmetric Difference.
Description: Print the symmetric difference
of two sets M and N in ascending order.
Points: 10.

'''


m = int(input())
set_m = set(map(int, input().split()))
n = int(input())
set_n = set(map(int, input().split()))

final_set = (set_m.union(set_n)).difference(set_m.intersection(set_n))

for i in sorted(list(final_set)):
    print(i)
