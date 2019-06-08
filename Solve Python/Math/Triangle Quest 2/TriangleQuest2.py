'''
Problem: Triangle Quest 2.
Description: Given an integer n.
Print a palindromic triangle of size n.
Points: 20.

'''

# The original answer is this one.
# But due to testings I had to separate them
# for i in range(1, int(input())+1):
#     print(((10**i - 1)//9)**2)


def draw_triangle(n):
    for i in range(1, n+1):
        print(((10**i - 1)//9)**2)


if __name__ == "__main__":
    draw_triangle(int(input()))
