from StringSplitAndJoin import split_and_join


def test_split_join_1():
    assert split_and_join('this is a string') == 'this-is-a-string'


def test_split_join_2():
    assert split_and_join('123 123') == '123-123'


def test_split_join_3():
    assert split_and_join('! @ # * ()') == '!-@-#-*-()'