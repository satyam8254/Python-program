tc=int(input())
for i in range(tc):
    n=int(input())
    arr=[int(x) for x in input().split()]
    arr1=[]
    for i in range(n):
        arr1.append(arr[i])
    arr1.sort()
    if n==2:
        print(abs(arr[0]-arr[1]))
        continue
    if arr[0]==arr1[n-1] and arr[n-1]==arr1[0] and n!=2:
        print(max(arr1[n-2]-arr1[0],arr1[n-1]-arr1[1]))
    else:
        print(arr1[n-1]-arr1[0])