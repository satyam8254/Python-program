#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hackerrankInString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def hackerrankInString(s):
    # Write your code here
    l1=[]
    l1.append(s)
    for i in range(len(l1)):
        if "hackerrank" in l1[i]:
            return "YES"
        else:
            return "NO"

s=input()
res=hackerrankInString(s)
print(res)
# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     q = int(input().strip())

#     for q_itr in range(q):
#         s = input()

#         result = hackerrankInString(s)

#         fptr.write(result + '\n')

#     fptr.close()