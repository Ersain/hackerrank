'''
Problem: gnitroS.
Description: Given a string S.
Sort S in this form:
lowerCase > upperCase > (odds > evens).digits.
E.g.
Sorting1234 -> ginortS1324.
Points: 40.

'''


def solve(string):
    lowers = sorted([i for i in string if i.islower()])
    uppers = sorted([i for i in string if i.isupper()])
    evens = sorted([i for i in string if i.isdigit() and int(i) % 2 == 0])
    odds = sorted([i for i in string if i.isdigit() and int(i) % 2 == 1])

    return ''.join((lowers + uppers + odds + evens))

# a = input()

# print(solve(a))


def test_solve_1():
    assert solve('Sorting1234') == 'ginortS1324'


def test_solve_2():
    assert solve('21abc3FEG5dHe') == 'abcdeEFGH1352'


def test_solve_3():
    assert solve('FooBar1337') == 'aoorBF1337'
