from FindAString import count_substring


def test_count():
    assert count_substring('ABCDCDC', 'CDC') == 2
    assert count_substring('HAHAHA', 'AHA') == 2


def test_count_2():
    assert count_substring('ROFL', 'LMAO') == 0
    assert count_substring('AAAA', 'AA') == 3


def test_count_3():
    assert count_substring('PainGain', 'ain') == 2
    assert count_substring('test', 't') == 2