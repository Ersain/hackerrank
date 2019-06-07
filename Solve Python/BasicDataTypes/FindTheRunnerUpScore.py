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

# if __name__ == '__main__':
#     n = int(input())
#     arr = map(int, input().split())

#     print(find(arr))


def test_find_1():
    assert find([3, 2, 2, 4, 1]) == 3
    assert find([1, 2]) == 1


def test_find_2():
    assert find([]) is None
    assert find([1]) is None


def test_find_3():
    assert type(find([3, 2, 1, 0])) is int
    assert type(find([6, 4, 1, 3, 2, 1, 0])) is int
