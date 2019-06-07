from IntegersComeInAllSizes import count


def test_count_1():
    assert count(1, 1, 1, 1) == 2
    assert count(1, 5, 1, 6) == 2


def test_count_2():
    assert count(2, 2, 2, 2) == 8
    assert count(2, 3, 2, 4) == 24


def test_count_3():
    assert count(3, 3, 3, 3) == 54
    assert count(3, 4, 3, 4) == 162
