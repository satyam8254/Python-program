n=int(input())
arr=list(map(int,input().split()[:n]))

maxDiff=max(arr)
minDiff=min(arr)
result=maxDiff-minDiff
print(result)

#time complexity = O(n)
#space complexity =O(1)