'''
Problem: Calendar Module.
Description: Given a date,
find what the day is on that date.
E.g. 05/MAY/2019 == Wednesday.
Points: 10.

'''

import calendar


def define_date(m, d, y):
    return list(calendar.day_name)[calendar.weekday(y, m, d)].upper()


if __name__ == "__main__":
    m, d, y = list(map(int, input().split()))
    print(define_date(m, d, y))
