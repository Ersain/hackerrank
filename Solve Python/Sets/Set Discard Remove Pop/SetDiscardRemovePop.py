'''
Problem: Set .discard(), .remove() & .pop().
Description: Usage of set.discard(),
set.remove(), set.pop().
Points: 10.

'''


def perform_command(set_1, command):
    command = command.split()
    if command[0] == 'pop':
        set_1.pop()
    elif command[0] == 'remove':
        set_1.remove(int(command[1]))
    elif command[0] == 'discard':
        set_1.discard(int(command[1]))


if __name__ == "__main__":
    n = int(input())
    s = set(map(int, input().split()))
    commands_num = int(input())

    for i in range(commands_num):
        perform_command(s, input())

    print(sum(s))
