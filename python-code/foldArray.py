import array
arr=array.array("i",[])
n=int(input())
for i in range(n):
    num=int(input())
    arr.append(num)
noOfFold=int(input())
for i in range(noOfFold):
    res=[]
    if len(arr)%2==0:
        loopRange=len(arr)//2
    else:
        loopRange=len(arr)//2+1
    for i in range(loopRange):
        if i!=(len(arr)-1-i):
            res.append(arr[i]+arr[len(arr)-1-i])
        else:
            res.append(arr[i])
    arr=res
print(len(arr))
for i in arr:
    print(i)       





# n=int(input())
# a=[]
# for x in range(n):
#     a.append(int(input()))
# folds=int(input())
# def folding(a):
#     if len(a)%2==0:
#         for i in range(len(a)//2):
#             a[i]+=a[len(a)-i-1]
#         return a[:(len(a)//2)]
#     if len(a)%2!=0:
#         for i in range(len(a)//2):
#             a[i]+=a[len(a)-i-1]
#         return a[:(len(a)//2)+1]
# for i in range(1,folds+1):
#     a=folding(a)
# print(len(a))    
# for x in a:
#     print(x) 


























# n=int(input())
# a=[]
# for x in range(n):
#     a.append(int(input()))
# folds=int(input())
# def folding(a):
#     if len(a)%2==0:
#         for i in range(len(a)//2):
#             a[i]+=a[len(a)-i-1]
#         return a[:(len(a)//2)]
#     if len(a)%2!=0:
#         for i in range(len(a)//2):
#             print(i)
#             a[i]+=a[len(a)-i-1]
#         return a[:(len(a)//2)+1]
# for i in range(1,folds+1):
#     a=folding(a)
# print(len(a))    
# for x in a:
#     print(x)