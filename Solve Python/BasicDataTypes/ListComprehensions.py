'''
Problem: List Comprehensions
Description: Read 4 integers i, j, k, n and
print a list of all possible coordinates (i, j, k)
where i+j+k != n.
Points: 10.

'''


def generate_list(x, y, z, n):
    if x >= 0 and y >= 0 and z >= 0:
        return [[i, j, k, ]
                for i in range(x+1)
                for j in range(y+1)
                for k in range(z+1)
                if i+j+k != n]
    return None


if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    print(generate_list(x, y, z, n))
