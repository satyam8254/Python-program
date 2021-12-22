n = int(input())
negative=0
i=0
arr=list(map(int,input().split()[:n]))
while(i<n):
    if arr[i]<0:
        negative=negative+1
    i=i+1
print(negative)