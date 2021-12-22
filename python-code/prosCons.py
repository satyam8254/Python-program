tc=int(input())
for i in range(tc):
    n=int(input())
    sumofallanger=0
    arr=[]
    for i in range(n):
        h,a=map(int,input().split())
        sumofallanger=sumofallanger+a
        arr.append((h,a))
    arr.sort(key=lambda x:(x[0]+x[1]),reverse=True)
    # print(arr)
    res=arr[0][0]+arr[0][1]+arr[1][0]+arr[1][1]-sumofallanger
    print(res)
