from IncorrectRegex import is_regex


def test_regex_1():
    assert is_regex('123') == True


def test_regex_2():
    assert is_regex('.*+') == False


def test_regex_3():
    assert is_regex('[0-9]') == True
