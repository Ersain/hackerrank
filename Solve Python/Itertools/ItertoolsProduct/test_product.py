from ItertoolsProduct import cartesian_product


def test_prod_1():
    assert list(cartesian_product([1, 2], [3, 4])) == [
        (1, 3), (1, 4), (2, 3), (2, 4)]


def test_prod_2():
    assert list(cartesian_product([1, 2, 3], [4, 5, 6])) == [
        (1, 4), (1, 5), (1, 6), (2, 4), (2, 5), (2, 6), (3, 4), (3, 5), (3, 6)]


def test_prod_3():
    assert list(cartesian_product([0], [1, 2])) == [(0, 1), (0, 2)]
