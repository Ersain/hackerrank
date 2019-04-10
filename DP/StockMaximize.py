#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the stockmax function below.
def stockmax(arr):
    n = len(arr)
    ans  = 0    
    locmax = arr[n-1]

    for i in range(n-2,-1,-1):
        if arr[i] < locmax:
            ans += locmax - arr[i]
        else:
            locmax = arr[i]
    return ans
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        prices = list(map(int, input().rstrip().split()))

        result = stockmax(prices)

        fptr.write(str(result) + '\n')

    fptr.close()
