import math
def minHeight(b,a):
        return math.ceil((2*a)/b)
tc=int(input())
for i in range(tc):
    b,a=map(int,input().split())
    height = minHeight(b, a)
    print(height)



# def minHeight(b,a):
#     for i in range(1,a):
#         h=i
#         if (1/2)*b*i==a:
#             h=i
#             break
#     return h   
# tc=int(input())
# for i in range(tc):
#     b,a=map(int,input().split())
# height = minHeight(b, a)
# print(height)