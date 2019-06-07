from SetUnion import set_union_len


def test_union_1():
    assert set_union_len({*range(6)}, {*range(6)}) == 6


def test_union_2():
    assert set_union_len({*range(10)}, {*range(15)}) == 15


def test_union_3():
    assert set_union_len({*range(1)}, {5, 2, 12, 123}) == 5
