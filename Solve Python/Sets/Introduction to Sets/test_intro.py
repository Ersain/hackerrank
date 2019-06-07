from IntroductionToSets import set_average


def test_avg_1():
    assert set_average([1, 1, 2, 3]) == 2


def test_avg_2():
    assert set_average([4, 4, 4, 5]) == 4.5


def test_avg_3():
    assert set_average([1, 4, 9, 16, 16]) == 7.5
