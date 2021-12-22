n,x=map(int,input().split())
arr=[int(x) for x in input().split()[:n]]
s=0
for i in range(len(arr)):
    s=s+arr[i]
flag=0
for i in range(len(arr)):
    if s-arr[i]==x:
        flag=1
    else:
        flag
if flag==1:
    print(1)
else:
    print(0)