'''
Problem: gnitroS.
Description: Given a string S.
Sort S in this form:
lowerCase > upperCase > (odds > evens).digits.
E.g.
Sorting1234 -> ginortS1324.
Points: 40.

'''


def sort_symbols(string):
    lowers = sorted([i for i in string if i.islower()])
    uppers = sorted([i for i in string if i.isupper()])
    evens = sorted([i for i in string if i.isdigit() and int(i) % 2 == 0])
    odds = sorted([i for i in string if i.isdigit() and int(i) % 2 == 1])

    return ''.join((lowers + uppers + odds + evens))


if __name__ == '__main__':
    a = input()

    print(sort_symbols(a))
