n= int(input())
arr=[]
flag=0
for i in range(n):
    num=int(input())
    arr.append(num)
for i in range(n):
    if (arr[i]>0 and arr[i-1]<=0):
        flag=1
    elif (arr[i]<0 and arr[i-1]>0):
        flag=1
    else:
        flag=0
if flag==1:
    print("True")
else:
    print("False")
