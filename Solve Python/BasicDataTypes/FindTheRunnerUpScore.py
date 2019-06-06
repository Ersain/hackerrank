'''
Problem: Find the runner-up score!
Description: Read an integer n and array arr,
print the runner-up score.
Points: 10.

'''


if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    print(sorted(list(set(arr)))[-2])
