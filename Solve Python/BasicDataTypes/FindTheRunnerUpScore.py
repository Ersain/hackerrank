'''
Problem: Find the runner-up score!
Description: Read an integer n and array arr,
print the runner-up score.
Points: 10.

'''


def find(arr):
    if len(arr) > 1:
        return sorted(list(set(arr)))[-2]
    return None


if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    print(find(arr))
