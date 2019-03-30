def print_formatted(number):
    # your code goes here
    for i in range(number):
        width = len("{0:b}".format(n))
        print('{:>{width}}'.format(i+1, width = width), end=' ')
        print('{:>{width}o}'.format(i+1, width = width), end=' ')
        print('{:>{width}X}'.format(i+1, width = width), end=' ')
        print('{:>{width}b}'.format(i+1, width = width))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
