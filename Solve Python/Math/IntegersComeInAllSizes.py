'''
Problem: Integers Come In All Sizes.
Description: Given 4 integers a, b, c, d.
Print a^b + c^d.
Points: 10.

'''


def count(num_a, num_b, num_c, num_d):
    return num_a**num_b + num_c**num_d


if __name__ == '__main__':
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())

    print(count(a, b, c, d))
