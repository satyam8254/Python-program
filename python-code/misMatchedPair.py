n=int(input())
arr=[int(x) for x in input().split()]
arr.sort()
left=0
right=n-1
lValue=None
rValue=None
mn=float('inf')
while left<right:
    diff=arr[left]+arr[right]
    if abs(diff)<mn:
        mn=abs(diff)
        lValue=arr[left]
        rValue=arr[right]
    if diff==0:
        break
    if diff<0:
        left+=1
    else:
        right-=1
print(lValue,rValue,mn)