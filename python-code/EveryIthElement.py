# n = int(input())
# list1=[]
# for i in range(n+1):
#     num=int(input())
#     list1.append(num)
# ith=int(num)
# sum=0
# for i in range(ith-1,n,ith):
#     sum=sum+list1[i]
# print(sum)

n=int(input())
list1=[]
sum=0
for i in range(1,n+1):
    num=int(input())
    list1.append(num)
ith=int(input())
for i in range(ith-1,n,ith):
    sum=sum+list1[i]
print(sum)

#time complexity = O(n/ith)
#space complexity =O(1)


