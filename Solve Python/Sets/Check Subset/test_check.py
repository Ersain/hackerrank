from CheckSubset import check_subset


def test_check_1():
    assert check_subset({*range(7)}, {*range(4)}) is False


def test_check_2():
    assert check_subset({*range(4)}, {*range(7)}) is True


def test_check_3():
    assert check_subset({123, 321, 677}, {321, 677, 123, 989}) is True
