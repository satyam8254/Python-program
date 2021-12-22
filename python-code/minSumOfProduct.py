n=int(input())
arr1=list(map(int,input().split()))
arr2=list(map(int,input().split()))
arr1.sort()
arr2.sort(reverse=True)
sm=0
for i in range(n):
    res=arr1[i]*arr2[i]
    sm=sm+res
print(sm)
# print(arr1)
# print(arr2)