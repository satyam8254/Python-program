#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    arr.sort()
    mn=0
    arr1=[]
    for i in range(len(arr)-1):
        mn=mn+arr[i]
    arr1.append(mn)
    mx=0
    for i in range(len(arr)-1,0,-1):
        mx=mx+arr[i]
    arr1.append(mx)
    print(*arr1)

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)