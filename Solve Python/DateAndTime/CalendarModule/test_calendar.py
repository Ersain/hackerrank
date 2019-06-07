from CalendarModule import define_date


def test_calendar_1():
    assert define_date(10, 5, 1999) == 'TUESDAY'


def test_calendar_2():
    assert define_date(10, 5, 2018) == 'FRIDAY'


def test_calendar_3():
    assert define_date(10, 5, 2019) == 'SATURDAY'
