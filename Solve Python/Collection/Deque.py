'''
Problem: Collections.deque().
Description: Perform the given commands
on a deque, e.g. append(), pop(),
popleft(), appendleft().

'''

from collections import deque

deq = deque()
num_choices = int(input())

for i in range(num_choices):
    operation = input().split()
    if operation[0] == 'append':
        deq.append(operation[1])
    elif operation[0] == 'pop':
        deq.pop()
    elif operation[0] == 'popleft':
        deq.popleft()
    elif operation[0] == 'appendleft':
        deq.appendleft(operation[1])

for i in deq:
    print(i, end=" ")
