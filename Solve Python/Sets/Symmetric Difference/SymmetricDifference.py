'''
Problem: Symmetric Difference.
Description: Print the symmetric difference
of two sets M and N in ascending order.
Points: 10.

'''


def set_symm_diff(set_1, set_2):
    return (set_1 ^ set_2)


if __name__ == "__main__":
    m = int(input())
    set_m = set(map(int, input().split()))
    n = int(input())
    set_n = set(map(int, input().split()))

    final_set = set_symm_diff(set_m, set_n)

    for i in sorted(list(final_set)):
        print(i)
