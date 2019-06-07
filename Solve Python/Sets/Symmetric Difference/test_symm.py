from SymmetricDifference import set_symm_diff


def test_symm_1():
    assert 2 not in set_symm_diff({2, 4, 11, 12}, {2, 4, 5, 9})


def test_symm_2():
    assert 5 not in set_symm_diff({2, 4, 11, 12}, {2, 4, 5, 9})


def test_symm_3():
    assert 11 in set_symm_diff({2, 4, 11, 12}, {2, 4, 5, 9})
