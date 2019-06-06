'''
Problem: Capitalize..
Points: 20.

'''


def solve(s):
    '''
    Return a capitilized version of a string,
    e.g.
    hello world => Hello World.
    '''
    for i in s.split():
        s = s.replace(i[0], i[0].upper())
    return s


def test_solve_1():
    assert solve('hello world') == 'Hello World'
    assert solve('asd') == 'Asd'


def test_solve_2():
    assert solve('     foo  bar ') == '     Foo  Bar '
    assert solve('a1b2c3') == 'A1b2c3'


def test_solve_3():
    assert solve('Checking') == 'Checking'
    assert solve('123') == '123'
