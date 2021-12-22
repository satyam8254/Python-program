tc=int(input())
for index in range(tc):
    n,d=map(int,input().split())
    arr=[int(x) for x in input().split()]
    d=d%n
    for i in range(d,n):
        print(arr[i],end=" ")
    for i in range(d):
        print(arr[i],end=" ")