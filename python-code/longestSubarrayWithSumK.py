def longestSubArr(arr,n,k):
    d={}
    sm=0
    maxLen=0
    for i in range(n):
        sm=sm+arr[i]
        if sm==k:
            maxLen=i+1
        elif (sm-k) in d:
            maxLen=max(maxLen,i-d[sm-k])
        if sm not in d:
            d[sm]=i
    return maxLen
n,k=map(int,input().split())
arr=[int(x) for x in input().split()[:n]]
print(longestSubArr(arr,n,k))