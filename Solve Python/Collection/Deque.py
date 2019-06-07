'''
Problem: Collections.deque().
Description: Perform the given commands
on a deque, e.g. append(), pop(),
popleft(), appendleft().
Points: 20.

'''
from collections import deque


def perform_cmd(d, command):
    command = command.split()
    if command[0] == 'append':
        d.append(int(command[1]))
    elif command[0] == 'pop':
        d.pop()
    elif command[0] == 'popleft':
        d.popleft()
    elif command[0] == 'appendleft':
        d.appendleft(int(command[1]))


if __name__ == '__main__':
    deq = deque()
    num_choices = int(input())

    for i in range(num_choices):
        operation = input()
        perform_cmd(deq, operation)

    print(deq)

#    for i in deq:
#        print(i, end=" ")
