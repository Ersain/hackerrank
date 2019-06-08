'''
Problem: Triangle Quest.
Description: Given an integer n.
Print a numerical triangle of height n-1.
Points: 20.

'''

# The original answer is this one.
# But due to testings I had to separate them
# for i in range(1,int(input())): #More than 2 lines will result in 0 score. Do not leave a blank line also
#     print((10**i)//9*i)


def draw_triangle(n):
    for i in range(1, n):
        print((10**i)//9*i)


if __name__ == "__main__":
    draw_triangle(int(input()))
