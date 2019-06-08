from Loops import squares


def test_squares_1():
    assert squares(9) == '0\n1\n4\n9\n16\n25\n36\n49\n64'


def test_squares_2():
    assert squares(4) == '0\n1\n4\n9'


def test_squares_3():
    assert squares(0) == ''
