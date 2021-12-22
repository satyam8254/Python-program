n=int(input())
if(n==0):
    print(-1)
else:
    list1=[]
    for i in range(n):
        num=int(input())
        list1.append(num)
    mx=0
    for i in list1:
        freq=list1.count(i)
        if(freq>mx):
            mx=freq
    list2=[]
    for i in list1:
        if(list1.count(i)==mx):
            list2.append(i)
    list2=list(set(list2))
    for i in list2:
        print(i)