import math
def calculation(n):
    sum=0
    for i in range(len(num)):
        sum=sum+(math.ceil(num[i]*0.07))
    print(sum)
n=int(input())
num=list(map(int,input().split()))
calculation(n)


