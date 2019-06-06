'''
Problem: Calendar Module.
Description: Given a date,
find what the day is on that date.
E.g. 05/MAY/2019 == Wednesday.
Points: 10.

'''

import calendar

m, d, y = list(map(int, input().split()))
print(list(calendar.day_name)[calendar.weekday(y, m, d)].upper())
