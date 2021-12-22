# def grainSplitting(arr):
#     res=[]
#     arr.sort()
#     div=sum(arr)//2
#     half=0
#     for i in range(len(arr)):
#         if half<div:
#             half=half+arr[i]
#             if half==div:
#                 res.append(arr[i+1:])  
#     return res
# n=int(input())
# print(n)
# for i in range(n):
#     arr=[int(x) for x in input().split()]
#     print(*(grainSplitting(arr)))





# tc = int(input())
# print(tc)
# for t in range(tc):
#     arr = [int(x) for x in input().split()]
#     arr.sort()
#     div = sum(arr)//2
#     vill1 = []
#     vill2 = []
#     i = 0
#     add = 0
#     while(add < div):
#         add += arr[i]
#         vill1.append(arr[i])
#         i += 1
#     while(i<len(arr)):
#         vill2.append(arr[i])
#         i += 1
#     print(*vill2)
