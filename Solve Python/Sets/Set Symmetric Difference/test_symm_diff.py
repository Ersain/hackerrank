from SetSymmetricDifference import set_symmetric_diff_len


def test_symm_diff_1():
    assert set_symmetric_diff_len({*range(3)}, {*range(1)}) == 2


def test_symm_diff_2():
    assert set_symmetric_diff_len({*range(10)}, {*range(4)}) == 6


def test_symm_diff_3():
    assert set_symmetric_diff_len({*range(15)}, {*range(3)}) == 12
