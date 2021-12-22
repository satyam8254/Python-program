n= int(input())
arr1=[]
arr2=[]
for i in range(n):
    num=int(input())
    arr1.append(num)
mn=min(arr1)
for i in range(len(str(mn))):
    rem=mn%10
    arr2.append(rem)
    mn=mn//10
sm=sum(arr2)
if sm%2==0:
    print(1)
else:
    print(0)


# n= int(input())
# arr1=[]
# for i in range(n):
#     num=int(input())
#     arr1.append(num)
# mn=min(arr1)
# arr2=[]
# if len(mn)==1:
#     arr2.append(mn)
#     if arr2[0]%2==0:
#         print(1)
#     else:
#         print(0)
# elif len(mn>1):
#     for i in range(len(mn)):
#         r=mn[i]%10
#         arr2.append(r)






