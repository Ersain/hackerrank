from PolarCoordinates import count_abs, count_phase


def test_abs():
    assert count_abs(3, 4) == 5
    assert count_abs(6, 8) == 10


def test_phase_1():
    assert count_phase(3, 4) > 0
    assert count_phase(6, 8) > 0


def test_phase_2():
    assert count_phase(6, 0) == 0
    assert count_phase(0, 8) > 1
