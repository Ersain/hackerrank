from WriteAFunction import is_leap


def test_leap_1():
    assert is_leap(1990) == False


def test_leap_2():
    assert is_leap(2000) == True


def test_leap_3():
    assert is_leap(2008) == True


def test_leap_4():
    assert is_leap(1999) == False
