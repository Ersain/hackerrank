'''
Problem: Set .intersection() Operation.
Description: Usage of set.intersection() method on sets.
Points: 10.

'''


def set_intersection_len(set_1, set_2):
    return len(set_1 & set_2)


if __name__ == "__main__":
    n = int(input())
    n_set = set(map(int, input().split()))
    b = int(input())
    b_set = set(map(int, input().split()))

    print(set_intersection_len(n_set, b_set))
