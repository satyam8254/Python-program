def thirdLargest(arr):
    arr=set(arr)
    if len(arr)>=3:
        for i in range(2):
            maxElement=max(arr)
            arr.remove(maxElement)
        return(max(arr))
    else:
        return "NA"
    
for _ in range(int(input())):
    size=int(input())
    arr=[int(x) for x in input().split()]
    print(thirdLargest(arr))































# def thirdLargest(arr,size):
#     if size<3:
#         return "NA"

#     for i in range(1,size):
#         j=i
#         while j>0 and arr[j]<arr[j-1]:
#             arr[j],arr[j-1]=arr[j-1],arr[j]
#             j=j-1
#     if arr[-1]==arr[-2]:
#         return "NA"
#     else:
#         return arr[-3]


# for _ in range(int(input())):
#     size=int(input())
#     arr=[int(x) for x in input().split()]
#     print(thirdLargest(arr,size))