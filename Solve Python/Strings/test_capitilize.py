from Capitilize import capitilize_words


def test_capitilize_words_1():
    assert capitilize_words('hello world') == 'Hello World'
    assert capitilize_words('asd') == 'Asd'


def test_capitilize_words_2():
    assert capitilize_words('     foo  bar ') == '     Foo  Bar '
    assert capitilize_words('a1b2c3') == 'A1b2c3'


def test_capitilize_words_3():
    assert capitilize_words('Checking') == 'Checking'
    assert capitilize_words('123') == '123'
