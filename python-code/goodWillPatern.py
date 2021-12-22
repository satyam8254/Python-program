
# m = (2*n)-2
# for i in range(0,n):
#     for j in range(0,m):
#         print(end=" ")
#     m=m-1
#     for j in range(0,i+1):
#         print("","$","*",end=" ")
#     print(" ")


# n= int(input())
# for i in range(n+1):
#     for j in range(n,0,-1):
#         if j>1:
#             print(" ",end="")
#         elif j%2==0:
#             print("$",end="")
#         else:
#             print("*",end="")
#     for j in range(1,i):
#         if j%2==0:
#             print("*",end="")
#         else:
#             print("$",end="")
#     print('')

# size = int(input())
# odd = "$*$"
# even = "*"
# for i in range(size):
#     print(" "*int(size-(i+1)),end="")
#     if(i%2==1):
#         print(odd)
#         newOdd = "$"+even+"$"
#         odd = newOdd
#     else:
#         print(even)
#         newEven = "*"+odd+"*"
#         even = newEven





n=int(input())
for i in range(n):
    print(" "*int(n-(i+1)),end="")
    if i==0:
        print("*")
    elif i%2==1:
        print("$*"*i+"$")
    elif i%2==0:
        print("*$"*i+"*") 

#time complexity = O(n)
#space complexity = O(1)















