from collections import deque
from Deque import perform_cmd


def test_perform_cmd_1():
    res = deque([1, 2, 3, 4])
    perform_cmd(res, 'pop')
    print(res)
    assert res == deque([1, 2, 3, ])


def test_perform_cmd_2():
    res = deque([])
    perform_cmd(res, 'append 5')
    print(res)
    assert res == deque([5, ])


def test_perform_cmd_3():
    res = deque([1, 2, 3, 4])
    perform_cmd(res, 'appendleft 5')
    print(res)
    assert res == deque([5, 1, 2, 3, 4])
