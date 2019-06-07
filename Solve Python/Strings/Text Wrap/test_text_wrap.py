from TextWrap import wrap


def test_wrap_1():
    assert wrap('ABCDE', 4) == 'ABCD\nE'


def test_wrap_2():
    assert wrap('FOOBAR', 3) == 'FOO\nBAR'


def test_wrap_3():
    assert wrap('HAHAHAHAHAHAHAHAHA', 6) == 'HAHAHA\nHAHAHA\nHAHAHA'
