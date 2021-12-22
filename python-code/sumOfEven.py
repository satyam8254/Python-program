n= int(input())
sumOfEven=0
arr=list(map(int,input().split()[:n]))
i=0
while(i<n):
    if arr[i]%2==0:
        sumOfEven=sumOfEven+arr[i]
    i=i+1
print(sumOfEven)
