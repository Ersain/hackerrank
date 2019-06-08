'''
Problem: Incorrect Regex.
Description: Given a regular expression S,
define whether S is valid regex or not.
Points: 20.

'''

import re


def is_regex(string):
    try:
        re.compile(string)
        return True
    except re.error:
        return False


if __name__ == "__main__":
    for i in range(int(input())):
        print(is_regex(input()))
