#!/bin/python3

import os
import sys

#
# Complete the getTotalX function below.
#
def gcd(a, b):
    while b:
        a, b = b, a%b
    return a

def gcd_arr(arr):
    for i in range(len(arr)-1):
        while arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]%arr[i+1]
        arr[i+1] = arr[i]
    return arr[-1]

def lcm_arr(arr):
    for i in range(1, len(arr)):
        arr[i] = arr[i-1]*arr[i]/gcd(arr[i-1], arr[i])
    return int(arr[-1])

def check(num, arr):
    for i in arr:
        if i%num!=0:
            return False
    return True

def getTotalX(a, b):
    #
    # Write your code here.
    #
    a_lcm = lcm_arr(a)
    counter = 0
    i = 1
    m = gcd_arr(b)
    temp = a_lcm
    while temp <= m:
        temp = a_lcm*i
        i += 1
        if check(temp, b):
            counter += 1
    return counter
