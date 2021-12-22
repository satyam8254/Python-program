#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    hour = s[:2]
    amPm = s[8:]
    if(hour == "12" and amPm == "AM"):
        hour = "00"
    elif(hour == "12" and amPm == "PM"):
        hour = "12"
    elif(amPm == "PM"):
        hour = int(hour)+12
        hour = str(hour)
    s = hour+s[2:8]
    print(s)


# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

s = input()

result = timeConversion(s)

    # fptr.write(result + '\n')

    # fptr.close()
