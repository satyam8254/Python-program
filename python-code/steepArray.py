#import array
#arr1=array.array("i",[])
arr1=[]
n= int(input())
#num=list(map,int(input().split()[:n]))
for i in range(n):
    num=int(input())
    arr1.append(num)
s=0
for i in range(len(arr1)):
    d=max(arr1[i:])-arr1[i]
    s=s+d
print(s)

