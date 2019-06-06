'''
Problem: "What's Your Name?".
Points: 10.

'''


def print_full_name(f_name, l_name):
    '''Get full name and greet'''
    return ('Hello {0} {1}!\
 You just delved into python.'.format(f_name, l_name))

# if __name__ == '__main__':
#     first_name = input()
#     last_name = input()
#     print_full_name(first_name, last_name)


def test_print_1():
    assert print_full_name('John', 'Doe') == 'Hello John Doe!\
 You just delved into python.'


def test_print_2():
    assert print_full_name('Alex', 'Hirsch') == 'Hello Alex Hirsch!\
 You just delved into python.'


def test_print_3():
    assert print_full_name('Harry', 'Kane') == 'Hello Harry Kane!\
 You just delved into python.'
