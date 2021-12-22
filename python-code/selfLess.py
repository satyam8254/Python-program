def selfLess(l1):
    left=[1]*len(l1)
    right=[1]*len(l1)
    for i in range(1,len(l1)):
        left[i]=left[i-1]*l1[i-1]
    for i in range(len(l1)-2,-1,-1):
        right[i]=right[i+1]*l1[i+1]
    res=[]
    for i in range(len(l1)):
        res.append(left[i]*right[i])
    return res

t = int(input())
for i in range(t):
    size=int(input())
    l1=list(map(int, input().split()[:size]))
    print(*selfLess(l1))























# tc=int(input())
# for i in range(tc):
#     size=int(input())
#     arr=[int(x) for x in input().split()[:size]]
#     if size==1:
#         print(1)
#     else:
#         res=[]
#         l1=[]
#         mul=1
#         for i in range(len(arr)):
#             arr=arr.remove(arr[i])
#             l1.append(arr[i+1])
#             #res.append(mul)
# print(*l1)



