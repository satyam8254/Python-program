n=int(input())
arr=[]
for i in range(n):
    num=int(input())
    arr.append(num)
x=int(input())
corrupt_pendrive=0
for i in range(n):
    if arr[i]<x:
        corrupt_pendrive+=arr[i]
print(corrupt_pendrive)

