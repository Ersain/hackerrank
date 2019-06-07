from SwapCase import swap_case


def test_swap_1():
    assert swap_case('Swap Case') == 'sWAP cASE'


def test_swap_2():
    assert swap_case('AhAhA') == 'aHaHa'


def test_swap_3():
    assert swap_case('FooBar') == 'fOObAR'
