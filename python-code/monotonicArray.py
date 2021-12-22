n=int(input())
l1=[]
for i in range(n):
    num=int(input())
    l1.append(num)
def isMonotonic(l1):
    return (all(l1[i]<=l1[i+1] for i in range(len(l1)-1)) or all(l1[i]>=l1[i+1] for i in range(len(l1)-1)))
print(isMonotonic(l1))
#flag=1       
    #for j in range(len(l1)):
#         flag
#     else:
#         flag=-1
# if flag==1 or len(l1)==1:
#     print("True")
# else:
#     print("False")

