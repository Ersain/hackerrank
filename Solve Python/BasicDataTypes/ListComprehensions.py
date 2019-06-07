'''
Problem: List Comprehensions
Description: Read 4 integers i, j, k, n and
print a list of all possible coordinates (i, j, k)
where i+j+k != n.
Points: 10.

'''


def solve(x, y, z, n):
    if x >= 0 and y >= 0 and z >= 0:
        return [[i, j, k, ]
                for i in range(x+1)
                for j in range(y+1)
                for k in range(z+1)
                if i+j+k != n]
    return None

# if __name__ == '__main__':
#     x = int(input())
#     y = int(input())
#     z = int(input())
#     n = int(input())

#     print(solve(x, y, z, n))


def test_solve_1():
    assert type(solve(1, 1, 1, 2)) is list
    assert solve(-1, 0, 0, 2) is None


def test_solve_2():
    assert solve(0, 0, 0, -1) == [[0, 0, 0]]
    assert solve(1, 1, 1, 2) == [
                                    [0, 0, 0],
                                    [0, 0, 1],
                                    [0, 1, 0],
                                    [1, 0, 0],
                                    [1, 1, 1]
                                ]


def test_solve_3():
    assert solve(2, 2, 2, 2) == [
                                    [0, 0, 0],
                                    [0, 0, 1],
                                    [0, 1, 0],
                                    [0, 1, 2],
                                    [0, 2, 1],
                                    [0, 2, 2],
                                    [1, 0, 0],
                                    [1, 0, 2],
                                    [1, 1, 1],
                                    [1, 1, 2],
                                    [1, 2, 0],
                                    [1, 2, 1],
                                    [1, 2, 2],
                                    [2, 0, 1],
                                    [2, 0, 2],
                                    [2, 1, 0],
                                    [2, 1, 1],
                                    [2, 1, 2],
                                    [2, 2, 0],
                                    [2, 2, 1],
                                    [2, 2, 2]
                                ]
