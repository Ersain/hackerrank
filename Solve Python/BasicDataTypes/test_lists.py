from Lists import use_command


def test_use_1():
    res = [3, 2, 1]
    use_command(res, 'sort')
    assert res == [1, 2, 3]


def test_use_2():
    res = [0, 1, 1, 2]
    use_command(res, 'append 3')
    assert res == [0, 1, 1, 2, 3]


def test_use_3():
    res = [1, 3, 3, 7]
    use_command(res, 'pop')
    assert res == [1, 3, 3]
