'''
Problem: "String Formatting".

'''


def print_formatted(number):
    '''
    Print the given number in
    Decimal, Octal,
    Hexadecimal, Binary.

    '''
    for i in range(number):
        width = len("{0:b}".format(number))
        print('{:>{width}}'.format(i+1, width=width), end=' ')
        print('{:>{width}o}'.format(i+1, width=width), end=' ')
        print('{:>{width}X}'.format(i+1, width=width), end=' ')
        print('{:>{width}b}'.format(i+1, width=width))
