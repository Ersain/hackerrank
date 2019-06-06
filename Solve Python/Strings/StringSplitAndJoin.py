'''
Problem: String Split and Join.
Points: 10.

'''


def split_and_join(line):
    '''
    Convert String:
    this is a string =>
    this-is-a-string

    '''
    return ('-'.join(line.split()))

# if __name__ == '__main__':
#     line = input()
#     result = split_and_join(line)
#     print(result)


def test_split_join_1():
    assert split_and_join('this is a string') == 'this-is-a-string'


def test_split_join_2():
    assert split_and_join('123 123') == '123-123'

def test_split_join_3():
    assert split_and_join('! @ # * ()') == '!-@-#-*-()'
