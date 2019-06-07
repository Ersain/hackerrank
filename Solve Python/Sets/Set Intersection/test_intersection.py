from SetIntersection import set_intersection_len


def test_inter_1():
    assert set_intersection_len({1, 2, 3, 4}, {5, 6, 7, 8}) == 0


def test_inter_2():
    assert set_intersection_len({*range(4)}, {*range(10)}) == 4


def test_inter_3():
    assert set_intersection_len({4, 2, 1, 7}, {7, 2}) == 2
