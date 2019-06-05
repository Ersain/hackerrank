'''
Problem: Incorrect Regex.
Description: Given a regular expression S,
define whether S is valid regex or not.

'''

import re

for i in range(int(input())):
    try:
        re.compile(input())
        print(True)
    except re.error:
        print(False)
