n = int(input())
arr=list(map(int,input().split()[:n]))
i=0
sum=0
while(i<n):
    sum=sum+arr[i]
    i=i+2
print(sum)







'''for i in range(len(arr)):
    count=arr[0]
    if arr[i]%2!=0:
        continue
    else:
        count=count+arr[i]
print(count)
'''
