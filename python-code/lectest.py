import array
a=array.array("i",[])
n=int(input("enter the size of array"))
for i in range(n):
    num=int(input("enter the element"))
    a.append(num)
temp=a[0]
for i in range(1,len(a)):
    temp1=a[i]
    a[i]=temp1
    temp=a[i]
    
