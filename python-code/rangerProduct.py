def rangerProduct(l1):
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
    print(*rangerProduct(l1))



    # if len(l1)==1:
    #     print(l1[0])
    # else:
    #     left=[0]*len(l1)
    #     left[0]=1
    #     right=[0]*len(l1)
    #     right[0]=1
    #     multiply=[0]*len(l1)
    #     for i in range(1,len(l1)):
    #         left[i]=l1[i-1]*left[i-1]
    #     for i in range(len(l1)-2,-1,-1):
    #         right[i]=l1[i+1]*right[i+1]
    #     for i in range(len(l1)):
    #         multiply[i]=left[i]*right[i]
    #     print(multiply,end=" ")