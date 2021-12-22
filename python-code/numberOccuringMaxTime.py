n= int(input())
list1=[]
count=1
res=-1
for i in range(n):
    num=int(input())
    list1.append(num)
for i in range(1,n):
    if list1[i]==list1[i-1]:
        count=count+1
        if count==4:
            res=list1[i]
            break
    else:
        count=1
print(res)



