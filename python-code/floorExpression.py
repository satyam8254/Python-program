import math
def sumofproduct(n):
    # Code here
    sum=0
    for i in range(1,n+1):
        x=i
        y=math.floor(n/x)
        p=x*y
        sum=sum+p
    return sum
n = int(input())
print(sumofproduct(n))