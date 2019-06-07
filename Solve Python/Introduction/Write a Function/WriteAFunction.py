'''
Problem: Write a function.
Points: 10.

'''


def is_leap(year):
    '''Gets a year and defines whether it is a leap year'''

    if year % 400 == 0:
        return True
    elif year % 4 == 0 and year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False


year = int(input())
print(is_leap(year))
