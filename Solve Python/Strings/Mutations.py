'''
Problem: Mutations.
Points: 10.

'''


def mutate_string(string, position, character):
    '''Attach a character at desired position in a string'''
    return string[:position] + character + string[(position+1):]

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
