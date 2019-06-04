'''
Problem: List Comprehensions
Description: Read 4 integers i, j, k, n and
print a list of all possible coordinates (i, j, k)
where i+j+k != n

'''


if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    print([[i, j, k, ]
          for i in range(x+1)
          for j in range(y+1)
          for k in range(z+1)
          if i+j+k != n])
