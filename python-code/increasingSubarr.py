n=int(input())
l1=[int(x) for x in input().split()[:n]]
index=0
maxLength=0
length=1
for i in range(1,len(l1)):
    if l1[i]>l1[i-1]:
        length=length+1
    else:
        if length>maxLength:
            maxLength=length
            index=i
        length=1
if length>maxLength:
    maxLength=length
    index=len(l1)
l=maxLength
start=index-maxLength+1
end=index
print(l,start,end)






















# l2=[]
# for i in range(0,len(l1)):
#     for j in range(i+1,len(l1)):    
#         if l1[j]==l1[i]:
#             l2.append(l1[i])
#         elif l1[j]>l1[j-1]:
#             l2.append(l1[j])
#             startingIndex=j
#         else:
#             break
# print(startingIndex)
# print(l2)



