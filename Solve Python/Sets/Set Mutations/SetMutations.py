'''
Problem: Set Mutations.
Description: Read operations and perform them on a set.
Points: 10.

'''


def perform_command(set_a, set_b, command):
    if command == 'intersection_update':
        set_a &= set_b
    elif command == 'update':
        set_a |= set_b
    elif command == 'symmetric_difference_update':
        set_a ^= set_b
    elif command == 'difference_update':
        set_a -= set_b


if __name__ == "__main__":
    num_of_a = int(input())
    a_set = set(map(int, input().split()))

    for i in range(int(input())):
        op_name = input().split()
        op_set = set(map(int, input().split()))
        perform_command(a_set, op_set, op_name[0])
    print(sum(a_set))
