from PythonDivision import int_division, division


def test_int_div():
    assert int_division(7, 5) == 1
    assert int_division(4, 3) == 1
    assert int_division(88, 20) == 4


def test_div():
    assert division(10, 4) == 2.5
    assert division(1001, 4) == 250.25
    assert division(147, 8) == 18.375
