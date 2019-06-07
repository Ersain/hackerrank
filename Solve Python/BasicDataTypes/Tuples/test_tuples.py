from Tuples import hash_tuple


def test_hash_1():
    temp = tuple()
    assert hash_tuple(temp) == hash(temp)


def test_hash_2():
    temp = (1, 2, 3, )
    assert hash_tuple(temp) == hash(temp)


def test_hash_3():
    temp = (None, )
    assert hash_tuple(temp) == hash(temp)
