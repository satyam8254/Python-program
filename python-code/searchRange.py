def first(arr,n,s):
    low=0
    high=n-1
    res=-1
    while (low<=high):
        mid =(low+high)//2
        if arr[mid]>=s:
            res=mid
            high=mid-1
        else:
            low=mid+1      
    return res

def Last(arr,n,e):
    low=0
    high=n-1
    res=-1
    while (low<=high):
        mid =(low+high)//2
        if arr[mid]<=e:
            res=mid
            low=mid+1
        else:
            high=mid-1
    return res

n=int(input())
arr=[int(x) for x in input().split()]
start,end=map(int,input().split())
f,l=first(arr,n,start),Last(arr,n,end)
if f<=l:
    print(f,l)
else:
    print(-1,-1)
















# def first(arr,n,start):
#     low=0
#     high=n-1
#     res=-1
#     while (low<=high):
#         mid =(low+high)//2
#         if start==arr[mid]:
#             res=mid
#             high=mid-1
#         elif start<arr[mid]:
#             high=mid-1
#         else:
#             low=mid+1
#     return res

# def Last(arr,n,end):
#     low=0
#     high=n-1
#     res=-1
#     while (low<=high):
#         mid =(low+high)//2
#         if end==arr[mid]:
#             res=mid
#             low=mid+1
#         elif end<arr[mid]:
#             high=mid-1
#         else:
#             low=mid+1
#     return res