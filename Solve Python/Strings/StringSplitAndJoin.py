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

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
