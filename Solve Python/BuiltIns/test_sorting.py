from Sorting import sort_symbols


def test_sort_symbols_1():
    assert sort_symbols('Sorting1234') == 'ginortS1324'


def test_sort_symbols_2():
    assert sort_symbols('21abc3FEG5dHe') == 'abcdeEFGH1352'


def test_sort_symbols_3():
    assert sort_symbols('FooBar1337') == 'aoorBF1337'
