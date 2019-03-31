# Enter your code here. Read input from STDIN. Print output to STDOUT
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
