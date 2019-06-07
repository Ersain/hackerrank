'''
Problem: "Tuples"
Description: Read an integer n and integers.
Create a tuple of this integers.
Compute hash() of the tuple and print.
Points: 10.

'''


def hash_tuple(tup):
    return hash(tup)

# if __name__ == '__main__':
#     n = int(input())
#     integer_list = map(int, input().split())

#     t = tuple(integer_list)
#     print(hash(t))


def test_hash_1():
    temp = tuple()
    assert hash_tuple(temp) == hash(temp)


def test_hash_2():
    temp = (1, 2, 3, )
    assert hash_tuple(temp) == hash(temp)


def test_hash_3():
    temp = (None, )
    assert hash_tuple(temp) == hash(temp)
