from FindingThePercentage import count_avg


def test_avg_1():
    temp = {'Ali': [50, 50, 50], 'Aidar': [75, 50, 99]}
    print(count_avg('Ali', temp))
    assert count_avg('Ali', temp) == 50


def test_avg_2():
    temp = {'Alina': [50, 100, 85], 'Malika': [52, 56, 60]}
    print(count_avg('Malika', temp))
    assert count_avg('Malika', temp) == 56


def test_avg_3():
    temp = {'Kamila': [50, 100, 84], 'Aruzhan': [52, 56, 60]}
    print(count_avg('Kamila', temp))
    assert count_avg('Kamila', temp) == 78
