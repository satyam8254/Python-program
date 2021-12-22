n,q=map(int,input().split())
arr=[int(x) for x in input().split()]
prefixSum=[arr[0]]
for i in range(1,len(arr)):
    prefixSum.append(arr[i]+prefixSum[-1])
for i in range(q):
    l,r=map(int,input().split())
    l,r=l-1,r-1
    if l-1>=0:
        print(prefixSum[r]-prefixSum[l-1])
    else:
        print(prefixSum[r])
