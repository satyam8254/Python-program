def insertTarget(arr,x):
    if x<arr[0]:
        return [x]+arr
    elif x>arr[len(arr)-1]:
        return arr+[x]
    else:
        for i in range(1,len(arr)):
            if x<=arr[i]:
                return arr[:i]+[x]+arr[i:]

tc=int(input())
for i in range(tc):
    n,x=map(int,input().split())
    arr=[int(x) for x in input().split()[:n]]
    print(*insertTarget(arr,x))