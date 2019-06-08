from PrintFunction import until_n


def test_n_1():
    assert until_n(5) == 12345


def test_n_2():
    assert until_n(9) == 123456789


def test_n_3():
    assert until_n(1) == 1
