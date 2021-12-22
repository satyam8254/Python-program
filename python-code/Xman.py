t=int(input())
arr=[]
for i in range(t):
    size=int(input())
    a=[int(x) for x in input().split()]
    arr.append(a)
for i in range(len(arr)):
    s=sum(arr[i])
    avg=s/len(arr[i])
    c=0
    for j in range(len(arr[i])):
        if int(arr[j])>avg:
            c=c+1
    print(c)
