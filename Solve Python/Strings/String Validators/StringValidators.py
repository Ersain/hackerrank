'''
Problem: "String Validators"
Description: Print true if -
a string has any alphanumeric,
a string has any alphabetical,
a string has any digits,
a string has any lowercase,
a string has any uppercase symbols.
Points: 10.

'''


def is_valid(s):
    print(any(i for i in s if i.isalnum()))
    print(any(i for i in s if i.isalpha()))
    print(any(i for i in s if i.isdigit()))
    print(any(i for i in s if i.islower()))
    print(any(i for i in s if i.isupper()))


if __name__ == '__main__':
    string = input()
    is_valid(string)
