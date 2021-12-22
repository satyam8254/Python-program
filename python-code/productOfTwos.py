n= int(input())
arr=[abs(int(x)) for x in input().split()[:n]]
revSum=[0]*len(arr)
revSum[len(arr)-1]=arr[len(arr)-1]
#print(revSum)
for i in range(len(arr)-2,-1,-1):
    revSum[i]=revSum[i+1]+arr[i]
    #print(revSum[i+1],"+",arr[i],"=",revSum)
#print(arr)
#print(revSum)
res=0
for i in range(len(arr)-2,-1,-1):
    res=res+arr[i]*revSum[i+1]
    #print(arr[i],"*",revSum[i+1],"=",res)
print(res)

























# arr1=[]
# for i in range(len(arr)):
#     arr1.append(abs(arr[i]))
# arr2=[]
# for i in range(len(arr1)):
#     for j in range(i+1,len(arr)):
#         m=arr1[i]*arr1[j]
#         arr2.append(m)
# # print(arr2)
# print(sum(arr2))