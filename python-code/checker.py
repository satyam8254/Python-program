for _ in range(int(input())):
    a=list(map(int,input().split()))
    n=int(input())
    e=list(map(int,input().split()))
    for i in a:
        if e in a:
            print(a.index(i))
    print(-1)


































# def checker(arr1,arr2,n):
#     res=[]
#     for i in range(n):
#         if arr2[i] in arr1:
#             res.append(arr1.index(arr2[i]))
#         else:
#             res.append(-1)
#     return res


# tc=int(input())
# for i in range(tc):
#     arr1=[int(x) for x in input().split()]
#     n=int(input())
#     for j in range(n):
#         arr2=[int(x) for x in input().split()[:n]]
#         print(checker(arr1,arr2,n))
    

