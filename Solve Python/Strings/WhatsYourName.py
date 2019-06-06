'''
Problem: "What's Your Name?".
Points: 10.

'''


def print_full_name(f_name, l_name):
    '''Get full name and greet'''
    print('Hello {0} {1}! You just delved into python.'.format(f_name, l_name))

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)
