from ListComprehensions import generate_list


def test_generate_list_1():
    assert type(generate_list(1, 1, 1, 2)) is list
    assert generate_list(-1, 0, 0, 2) is None


def test_generate_list_2():
    assert generate_list(0, 0, 0, -1) == [[0, 0, 0]]
    assert generate_list(1, 1, 1, 2) == [
        [0, 0, 0],
        [0, 0, 1],
        [0, 1, 0],
        [1, 0, 0],
        [1, 1, 1]
    ]


def test_generate_list_3():
    assert generate_list(2, 2, 2, 2) == [
        [0, 0, 0],
        [0, 0, 1],
        [0, 1, 0],
        [0, 1, 2],
        [0, 2, 1],
        [0, 2, 2],
        [1, 0, 0],
        [1, 0, 2],
        [1, 1, 1],
        [1, 1, 2],
        [1, 2, 0],
        [1, 2, 1],
        [1, 2, 2],
        [2, 0, 1],
        [2, 0, 2],
        [2, 1, 0],
        [2, 1, 1],
        [2, 1, 2],
        [2, 2, 0],
        [2, 2, 1],
        [2, 2, 2]
    ]
