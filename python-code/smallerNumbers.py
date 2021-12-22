def smallerNumber(arr,n):
    d={}
    for i in arr:
        if i in d:
            d[i]=d[i]+1
        else:
            d[i]=1
    smaller=0
    for i in sorted(d.keys()):
        temp=d[i]
        d[i]=smaller
        smaller=smaller+temp
    for i in arr:
        print(d[i])
n= int(input())
arr=[]
for i in range(n):
    num=int(input())
    arr.append(num)
smallerNumber(arr,n)













# n=int(input())
# arr=[]
# for i in range(n):
#     num=int(input())
#     arr.append(num)
# arr2=[]
# cnt=0
# for i in range(len(arr)):
#     for j in range(len(arr)):
#         if arr[j]!=arr[i] and arr[j]<arr[i]:
#             cnt=cnt+1
#     arr2.append(cnt)
# for i in range(len(arr2)):
#     print(arr2[i])
