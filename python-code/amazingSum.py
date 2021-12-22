n = int(input())
intValue=[]
flag=0
for i in range(n):
    num = int(input())
    intValue.append(num)
for i in range(0,n-1):
    if (intValue[i]+intValue[i+1]) > 100:
       flag=1
       break
    else:
        flag=0
if flag ==1:
    print("True")
else:
    print("False")