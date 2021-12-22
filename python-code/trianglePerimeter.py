tc=int(input())
a=0
b=0
c=0
flag=False
for i in range(tc):
    arr=[int(x) for x in input().split()]
    arr.sort(reverse=True)
    if len(arr)>3:
        for i in range(len(arr)-2):
            a=arr[i]
            b=arr[i+1]
            c=arr[i+2]
            if a<(b+c) and b<(a+c) and c<(a+b):
                flag=True
                break
            else:
                flag=False
    elif len(arr)==3:
        a=arr[0]
        b=arr[1]
        c=arr[2]
        if a<(b+c) and b<(a+c) and c<(a+b):
            flag=True
        else:
            flag=False
    else:
        flag=False
    if flag:
        print(a+b+c)
    else:
        print(0)

