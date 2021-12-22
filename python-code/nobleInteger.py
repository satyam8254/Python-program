n=int(input())
list1=[]
for i in range(n):
    num=int(input())
    list1.append(num)
flag=0
if n>=2:        
    for i in range(len(list1)):
        count=0
        for j in range(len(list1)):
            if list1[j]>list1[i]:
                count=count+1
        if count==list1[i]:
            flag=1
if flag==1:
    print(1)
else:
    print(-1)
