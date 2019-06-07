'''
Problem: Map and Lambda Function.
Description: Given an integer n.
Print the fibonacci sequence until n,
where each member of the sequence is x^3.
E.g.
5 -> [0, 1, 1, 8, 27]

Points: 20.


'''


def cube(x): return x*x*x


def fibonacci(n):
    fib = [0]*n

    if n > 1:
        fib[1] = 1

        for i in range(2, n):
            fib[i] = fib[i-1]+fib[i-2]

    return fib
