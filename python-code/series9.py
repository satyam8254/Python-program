# n=int(input())
# num=9
# sum=0
# if n==1:
#     print(num)
# for i in range(n):
#     if n>1:
#         sum= sum+num
#         num=(num*10)+9
# print(sum)

n=int(input())
sum=(10*(10**n-1))//9-n
print(sum)