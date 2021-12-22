# n=int(input())
# s=input()
# l=list(input().split())
# result=1
# for i in s:
#     flag=0
#     for j in l:
#         if(i==j):
#             flag=1
#             break
#     if (flag==0):
#         result=0
#         break
# if(result==1):
#     print("true")
# else:
#     print("false")

# #time complexity = O(n*n)
# #space complexity = O(1)


size = int(input())
name = input()
list1 = list(map(str, input().split()))
length = 0
for i in range(len(name)):
    if(name[i] in list1):
        length+=1
    else:
        print("false")
        break
if(length == len(name)):
    print("true")

# #time complexity = O(n)
# #space complexity = O(1)