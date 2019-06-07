from AnyOrAll import check


def test_check_1():
    assert check(['12', '9', '61', '5', '14']) is True


def test_check_2():
    assert check(['1', '2', '3', '4', '5', '-9']) is False


def test_check_3():
    assert check([0]) is False
