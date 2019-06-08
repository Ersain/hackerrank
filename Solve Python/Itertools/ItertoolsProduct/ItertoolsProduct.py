'''
Problem: itertools.product()
Description: Given two lists A and B,
Print their Cartesian Product.
Points: 10.

'''


from itertools import product


def cartesian_product(arr1, arr2):
    return product(arr1, arr2)


if __name__ == "__main__":
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    res = cartesian_product(a, b)

    for i in res:
        print(i, end=" ")
