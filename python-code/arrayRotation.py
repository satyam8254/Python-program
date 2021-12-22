def arrRotation(arr,n,rotate):
    result=[0]*n
    for i in range(n):
        result[(i+rotate)%n]=arr[i]
    return result
n,q=map(int,input().split())
arr=[int(x) for x in input().split()]
res=0
for i in range(q):
    direction,noOfRotation=input().split()
    if direction=="L":
        res=res-int(noOfRotation)
    elif direction=="R":
        res=res+int(noOfRotation)
print(*arrRotation(arr,n,res))



















# n,q=map(int,input().split())
# arr=list(map(int,input().split()[:n]))
# for i in range(q):
#     direction,noOfRotation=input().split()
#     noOfRotation=int(noOfRotation)
#     if direction=="L":
#         arr=arr[noOfRotation:]+arr[:noOfRotation]
#     if direction=="R":
#         arr=arr[-noOfRotation:]+arr[:-noOfRotation]
# print(*arr)