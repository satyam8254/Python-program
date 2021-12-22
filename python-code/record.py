n= int(input())
arr=[int(x) for x in input().split()]
mn,mx=arr[0],arr[0]
# mn1=[0]
# mx1=[0]
record=[0,0]
for i in range(1,n):
    if arr[i]<mn:
        mn=arr[i]
        #mn1[0]=mn1[0]+1
        record[0]=record[0]+1
    elif arr[i]>mx:
        mx=arr[i]
        #mx1[0]=mx1[0]+1
        record[1]=record[1]+1
print(record[1],record[0])
