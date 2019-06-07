'''
Problem: Set Mutations.
Description: Read operations and perform them on a set.
Points: 10.

'''


num_of_a = int(input())
a_set = set(map(int, input().split()))

for i in range(int(input())):
    op_name = list(input().split())
    op_set = set(map(int, input().split()))
    if op_name[0] == 'intersection_update':
        a_set &= op_set
    elif op_name[0] == 'update':
        a_set |= op_set
    elif op_name[0] == 'symmetric_difference_update':
        a_set ^= op_set
    elif op_name[0] == 'difference_update':
        a_set -= op_set
print(sum(a_set))
