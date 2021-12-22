# n=int(input())
# arr=[]
# for i in range(n):
#     num=int(input())
#     arr.append(num)
# for j in range(0,len(arr),1):
#     if arr[j]==arr[j+1]:
#         continue
#     else:
#         print(arr[j])
#         break

# n=int(input())
# list1=[]
# for i in range(n):
#     num=int(input())
#     list1.append(num)
# for j in range(len(list1)):
#     if list1[j]==list1[j+1]:
#         continue
#     else:
#         print(list1[j])
#         break



n=int(input())
list1=[]
for i in range(n):
    num=int(input())
    list1.append(num)
for i in range(n):
    if (list1.count(list1[i])==2):
        continue
    else:
        print(list1[i])

#time complexity = O(n)
#space complexity = O(n)