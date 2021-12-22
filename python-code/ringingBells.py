import math
n=int(input())
arr=[int(x) for x in input().split()]
res=arr[0]
for i in range(n):
    gcd=math.gcd(res,arr[i])
    res=((res*arr[i])//gcd)
print(res)