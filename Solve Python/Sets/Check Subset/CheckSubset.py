'''
Problem: Check Subset.
Description: Check if a given set A is a subset of a set B.
Points: 10.

'''


def check_subset(set_1, set_2):
    return set_1.issubset(set_2)


if __name__ == "__main__":
    for i in range(int(input())):
        len_a = int(input())
        a_set = set(map(int, input().split()))
        len_b = int(input())
        b_set = set(map(int, input().split()))
        print(check_subset(a_set, b_set))
