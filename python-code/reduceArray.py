import array
arr=array.array("i",[])
n=int(input())
for i in range(n):
    num=int(input())
    arr.append(num)

if n>1:
    m=arr[0]+arr[1]
    for i in range(2,n):
        if i%2==0:
            m=m-arr[i]
        else:
            m=m+arr[i]
    print(m)
else:
    print(arr[0])
