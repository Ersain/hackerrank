'''
Problem: Mutations.
Points: 10.

'''


def wrap(string, max_width):
    '''Wrap the string into a paragraph of the given width'''
    res = ''

    for i in range(len(string)):
        if i > 0 and i % max_width == 0:
            res += '\n'
        res += string[i]
    return res

# if __name__ == '__main__':
#     string, max_width = input(), int(input())
#     result = wrap(string, max_width)
#     print(result)


def test_wrap_1():
    assert wrap('ABCDE', 4) == 'ABCD\nE'

def test_wrap_2():
    assert wrap('FOOBAR', 3) == 'FOO\nBAR'

def test_wrap_3():
    assert wrap('HAHAHAHAHAHAHAHAHA', 6) == 'HAHAHA\nHAHAHA\nHAHAHA'
