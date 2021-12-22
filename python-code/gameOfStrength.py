def game(arr,n):
    arr.sort(reverse=True)
    res=0
    m=n-1
    for i in arr:
        res+=i*m
        m=m-2
    return((res%(1000000007)*max(arr)%1000000007)%1000000007)



n=int(input())
for i in range(n):
    size=int(input())
    arr=[int(x) for x in input().split()]
    print(game(arr,size))



















# tc=int(input())
# for i in range(tc):
#     noOfBox=int(input())
#     arr=[int(x) for x in input().split()[:noOfBox]]
#     arr.sort()
#     res=0
#     for i in range(len(arr)-1,0,-1):
#         res=res+abs((arr[i]*i)-(arr[i]*(len(arr)-i-1)))%1000000007
#     mx=max(arr)
#     res=res*mx
#     print(res%1000000007)


























# tc=int(input())
# for i in range(tc):
#     noOfBox=int(input())
#     arr=[int(x) for x in input().split()[:noOfBox]]
#     res=0
#     for i in range(len(arr)-1):
#         for j in range(i+1,len(arr)):
#             res=res+abs(arr[i]-arr[j])
#     mx=max(arr)
#     res=res*mx
#     print(res%1000000007)


