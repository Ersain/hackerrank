from FindTheRunnerUpScore import find


def test_find_1():
    assert find([3, 2, 2, 4, 1]) == 3
    assert find([1, 2]) == 1


def test_find_2():
    assert find([]) is None
    assert find([1]) is None


def test_find_3():
    assert type(find([3, 2, 1, 0])) is int
    assert type(find([6, 4, 1, 3, 2, 1, 0])) is int
