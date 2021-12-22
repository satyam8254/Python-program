k=int(input())
listA=[]
n=int(input())
flag= False
for i in range(n):
    num=int(input())
    listA.append(num)
for j in range(len(listA)):
    if listA[j] == k:
        print(j)
        flag=True
        break
if flag==False:
    print(-1)
        


