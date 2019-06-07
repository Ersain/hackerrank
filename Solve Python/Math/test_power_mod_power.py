from PowerModPower import count_pow, count_pow_mod


def test_count_pow():
    assert count_pow(3, 3) == 27
    assert count_pow(2, 10) == 1024


def test_count_pow_mod():
    assert count_pow_mod(3, 3, 2) == 1
    assert count_pow_mod(2, 10, 5) == 4


def test_count():
    assert count_pow(3, 2) > count_pow_mod(3, 2, 2)
    assert count_pow(7, 3) > count_pow_mod(7, 3, 10)
