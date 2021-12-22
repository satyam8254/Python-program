# def rotate(l,n): 
#     list2=[]
#     if n>len(l):
#             pass
#     else:
#         for i in range(n,len(l)):                
#             list2.append(list1[i])
#         for i in range(0,n):
#             list2.append(l[i])
#         #return list2
#         for i in list2:
#             print(i)    
# list1=list(map(int,input().split()))
# n=int(input())
# print(rotate(list1,n))


def rotate(l,n):
    for i in range(n):
        temp=(l[0])
        l.remove(l[0])
        l.append(temp)
    for i in l:
        print(i)
l=list(map(int,input().split()))
n=int(input())
rotate(l,n)