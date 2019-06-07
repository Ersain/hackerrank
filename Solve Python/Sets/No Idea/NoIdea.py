'''
Problem: No Idea!
Description: Given a list of integers
and 2 disjoint sets A and B.
You have initial happiness = 0.
For each integer i,
where i in A, your happiness increments,
and if i in B, decrements.
Print you final happiness.
Points: 50.

'''


def count_happiness(arr, set_1, set_2):
    happiness = 0
    for i in arr:
        if i in set_1:
            happiness += 1
        elif i in set_2:
            happiness -= 1
    return happiness


if __name__ == "__main__":
    n, m = map(int, input().split())
    list_int = list(map(int, input().split()))
    set_a = set(map(int, input().split()))
    set_b = set(map(int, input().split()))

    print(count_happiness(list_int, set_a, set_b))
