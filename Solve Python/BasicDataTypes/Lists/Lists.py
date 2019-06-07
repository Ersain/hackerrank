'''
Problem: "Lists"
Description: Read an integer n and
list commands, e.g. remove, append, etc.
Perform the commands in the order on a list.
Points: 10.

'''


def use_command(arr, command):
    command = command.split()

    if command[0] == 'insert':
        arr.insert(int(command[1]), int(command[2]))
    elif command[0] == 'print':
        print(arr)
    elif command[0] == 'remove':
        arr.remove(int(command[1]))
    elif command[0] == 'append':
        arr.append(int(command[1]))
    elif command[0] == 'sort':
        arr.sort()
    elif command[0] == 'pop':
        arr.pop()
    elif command[0] == 'reverse':
        arr.reverse()


if __name__ == '__main__':
    N = int(input())

    a_list = []

    for i in range(N):
        op = input()
        use_command(a_list, op)
