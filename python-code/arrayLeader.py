# n=int(input())
# arr=[]
# for i in range(n):
#     num=int(input())
#     arr.append(num)
# arr2=[]
# #mx=arr[0]
# for i in range(len(arr)-1,0):
#     if arr[i]<=arr[i+1]:
#         continue
#     elif arr[i]>=arr[i+1]:
#         mx=arr[i]
#         arr2.append(mx)
# print(arr2)














n=int(input())
arr=[]
for i in range(n):
    num=int(input())
    arr.append(num)
mx=float('-inf')
for i in range(len(arr)-1,-1,-1):
    mx=max(mx,arr[i])
    if arr[i]==mx:
        print(arr[i])