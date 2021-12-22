def first(arr,n,x):
    low=0
    high=n-1
    res=-1
    while (low<=high):
        mid =(low+high)//2
        if x==arr[mid]:
            res=mid
            high=mid-1
        elif x<arr[mid]:
            high=mid-1
        else:
            low=mid+1
    return res

def Last(arr,n,x):
    low=0
    high=n-1
    res=-1
    while (low<=high):
        mid =(low+high)//2
        if x==arr[mid]:
            res=mid
            low=mid+1
        elif x<arr[mid]:
            high=mid-1
        else:
            low=mid+1
    return res



n=int(input())
arr=[int(x) for x in input().split()]
x=int(input())
print(first(arr,n,x),Last(arr,n,x))
# print(Last(arr,n,x))


















# def first(arr,n,x):
#     low=0
#     high=n-1
#     res=-1
#     while (low<=high):
#         mid =(low+high)//2
#         if arr[mid]>x:
#             high=mid-1
#         elif arr[mid]<x:
#             low=mid+1
#         else:
#             res=mid
#             high=mid+1
#     return res








# def Last(arr,n,x):
#     low=0
#     high=n-1
#     res=-1
#     while (low<=high):
#         mid =(low+high)//2
#         if arr[mid]>x:
#             high=mid-1
#         elif arr[mid]<x:
#             low=mid+1
#         else:
#             res=mid
#             low=mid+1
#     return res









    # f=-1
    # l=-1
    # for i in range(n):
    #     if x!=arr[i]:
    #         continue
    #     if f==-1:
    #         f=i
    #     l=i
    # if f!=-1:
    #     return(f,l)