noOfIcon=int(input())
list1=[]
for i in range(noOfIcon):
    icon=int(input())
    list1.append(icon)
list2=[]
nOfPixelInIcon=int(input())
for i in range(nOfPixelInIcon):
    checkIcon=int(input())
    list2.append(checkIcon)
count=0
if nOfPixelInIcon>0:
    for i in range(noOfIcon-nOfPixelInIcon+1):
        arr=[]
        for j in range(i,i+nOfPixelInIcon):
            arr.append(list1[j])
        if arr==list2:
            count=count+1
print(count)

