# n=int(input())
# m=((2*n)-2)
# for i in range(0,n):
#     for j in range(m):
#         print(end=" ")
#     m=m-1
#     for j in range(0,i+1):    
#         print("*",end=" ")
#     print(" ")
# m=(n-2)
# for i in range(n,-1,-1):
#     for j in range(m,0,-1):
#         print(end=" ")
#     m=m+1
#     for j in range(0,i+1):    
#         print("*",end=" ")
#     print(" ")

# n=int(input())
# for i in range(1,n+1):
#     for j in range(n,0,-i):
#         print(" ",end="")
#     for j in range(1,i+1):
#         print("*",end="")
#     print()

n = int(input())
for i in range(n):
    print(" "*(n-i), "*"*(i*2+1))
for i in range(n-2, -1, -1):
    print(" "*(n-i), "*"*(i*2+1))















    
