'''
Problem: Any or All.
Description: Given a list of integers,
If all the integers are positive,
then check if any integer is a palindromic integer..
Points: 20.

'''


def check(arr):
    return all(int(i) > 0 for i in arr) and any(i == i[::-1] for i in arr)


if __name__ == '__main__':
    N = int(input())
    integers = input().split()
    print(check(integers))
