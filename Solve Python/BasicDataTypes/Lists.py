'''
Problem: "Lists"
Description: Read an integer n and
list commands, e.g. remove, append, etc.
Perform the commands in the order on a list.
Points: 10.

'''


if __name__ == '__main__':
    N = int(input())

    a_list = []

    for i in range(N):
        op = input()

        op_list = op.split()

        if op_list[0] == 'insert':
            a_list.insert(int(op_list[1]), int(op_list[2]))
        elif op_list[0] == 'print':
            print(a_list)
        elif op_list[0] == 'remove':
            a_list.remove(int(op_list[1]))
        elif op_list[0] == 'append':
            a_list.append(int(op_list[1]))
        elif op_list[0] == 'sort':
            a_list.sort()
        elif op_list[0] == 'pop':
            a_list.pop()
        elif op_list[0] == 'reverse':
            a_list.reverse()
