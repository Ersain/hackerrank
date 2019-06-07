from SetDifference import set_diff_len


def test_diff_1():
    assert set_diff_len({*range(6)}, {*range(3)}) == 3


def test_diff_2():
    assert set_diff_len({*range(10)}, {*range(5)}) == 5


def test_diff_3():
    assert set_diff_len({*range(18)}, {*range(3)}) == 15
