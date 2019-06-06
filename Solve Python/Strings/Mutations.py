'''
Problem: Mutations.
Points: 10.

'''


def mutate_string(string, position, character):
    '''Attach a character at desired position in a string'''
    return string[:position] + character + string[(position):]

# if __name__ == '__main__':
#     s = input()
#     i, c = input().split()
#     s_new = mutate_string(s, int(i), c)
#     print(s_new)


def test_mutate_1():
    assert mutate_string('London', 3, ', ') == 'Lon, don'

def test_mutate_2():
    assert mutate_string('123123123123', 6, ' ') == '123123 123123'

def test_mutate_3():
    assert mutate_string('!@#$%^', 5, '/') == '!@#$%/^'