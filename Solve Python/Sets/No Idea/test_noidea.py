from NoIdea import count_happiness


def test_noidea_1():
    assert count_happiness([1, 5, 3], {3, 1}, {5, 7}) == 1


def test_noidea_2():
    assert count_happiness([1, 2, 3, 4, 5], {1, 2, 3}, {5}) == 2


def test_noidea_3():
    assert count_happiness([1, 2, 3, 4, 5], {5, 4, 3}, {0}) == 3
