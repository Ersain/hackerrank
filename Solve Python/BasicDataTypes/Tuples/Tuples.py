'''
Problem: "Tuples"
Description: Read an integer n and integers.
Create a tuple of this integers.
Compute hash() of the tuple and print.
Points: 10.

'''


def hash_tuple(tup):
    return hash(tup)


if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())

    t = tuple(integer_list)
    print(hash(t))
