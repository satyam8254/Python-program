def strongestLink(n,arr):
    maxSoFar=arr[0]
    maxEnding=0
    start=0
    end=0
    s=0
    for i in range(n):
        maxEnding=maxEnding+arr[i]
        if maxSoFar<maxEnding:
            maxSoFar=maxEnding
            start=s
            end=i
        if maxEnding<0:
            maxEnding=0
            s=i+1    
    return (start,end,maxSoFar)
      
n=int(input())
arr=[int(x) for x in input().split()]
print(*(strongestLink(n,arr)))