def minAbsDiff(arr):
    arr.sort()
    minDiff=abs(arr[0]-arr[1])
    for i in range(len(arr)-1):
        diff=abs(arr[i]-arr[i+1])
        if diff<minDiff:
            minDiff=diff
    print(minDiff)

n=int(input())
arr=[int(x) for x in input().split()]
minAbsDiff(arr)





# def minAbsDiff(arr,n):
#     diff=float('inf')
#     arr1=[]
#     for i in range(1,n):
#         j=i
#         while j>0 and abs(arr[j]-arr[j-1])<diff:
#             diff=abs(arr[j]-arr[j-1])
#             arr1.append(diff)
#             j=j-1
#     print(min(arr1))
# n=int(input())
# arr=[]
# for i in range(n):
#     num=int(input())
#     arr.append(num)
# minAbsDiff(arr,n)
































# n=int(input())
# arr=[]
# for i in range(n):
#     num=int(input())
#     arr.append(num)
# firstMin=min(arr)
# arr.remove(firstMin)
# secondMin=min(arr)
# arr.remove(secondMin)
# print(abs(secondMin-firstMin))