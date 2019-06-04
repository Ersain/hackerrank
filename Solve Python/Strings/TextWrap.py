'''
Problem: Mutations

'''


def wrap(string, max_width):
    '''Wrap the string into a paragraph of the given width'''
    res = ''

    for i in range(len(string)):
        if i > 0 and i % max_width == 0:
            res += '\n'
        res += string[i]
    return res

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
