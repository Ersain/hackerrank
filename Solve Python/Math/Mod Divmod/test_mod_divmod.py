from ModDivmod import int_division, mod_division, int_division_mod_tuple


def test_div():
    assert int_division(5, 6) == 0
    assert int_division(13, 5) == 2


def test_mod():
    assert mod_division(5, 2) == 1
    assert mod_division(20, 3) == 2


def test_divmod():
    assert int_division_mod_tuple(7, 3) == (2, 1)
    assert int_division_mod_tuple(29, 21) == (1, 8)
