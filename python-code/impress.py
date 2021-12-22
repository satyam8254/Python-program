from sys import stdin,stdout
def Which_Day(a, x):
    left = 0 
    right = len(a)-1
    while left<=right:
    	mid = (left+right)//2
    	if a[mid]>x:
    		right=mid-1
    	elif a[mid]<x:
    		left=mid+1
    	else:
    		return mid
    return left

n,q = map(int,stdin.readline().split())
a = list(map(int,stdin.readline().split()))
for i in range(n):
    if i!=0:
        a[i] = a[i-1]+a[i]
k = list(map(int,stdin.readline().split()))
for i in range(q):
    ans = Which_Day(a,k[i])+1
    stdout.write(str(ans)+"\n")