def inversionCount(arr, left, right):
    count = 0
    if right > left:
        mid = (left + right) // 2
        count += inversionCount(arr, left, mid)
        count += inversionCount(arr, mid + 1, right)
        count += merge(arr, left, mid, right)
    return count
def merge(arr, left, mid, right):
    sorted = [0] * (right - left + 1)
    inv_count = 0
    i = left
    j = mid + 1
    k = 0
    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            inv_count += (right - j + 1)
            sorted[k] = arr[i]
            i += 1
        else: # arr[i] > arr[j] and i < j
            sorted[k] = arr[j]
            j += 1
        k += 1
    while i <= mid:
        sorted[k] = arr[i]
        i += 1
        k += 1
    while j <= right:
        sorted[k] = arr[j]
        j += 1
        k += 1
    for i in range(left,right+1):
    	arr[i]=sorted[i-left]
    return inv_count
n=int(input())
arr = [int(x) for x in input().split()]
print(inversionCount(arr, 0, len(arr) - 1))























# def sortedPair(arr):
#     if len(arr)>1:
#         mid=len(arr)//2
#         left=arr[:mid]
#         right=arr[mid:]
#         sortedPair(left)
#         sortedPair(right)
#         i=0
#         j=0
#         cnt=0
#         while i<len(left) and j<len(right):
#             if left[i]<=right[j]:
#                 cnt=cnt+1
#                 i=i+1
#         return cnt
# n = int(input())
# arr = [int(x) for x in input().split()[:n]]
# print(sortedPair(arr))
    


















# n=int(input())
# arr=[int(x) for x in input().split()[:n]]
# cnt=0
# for i in range(len(arr)):
#     for j in range(i+1,len(arr)):
#         if arr[i]<=arr[j]:
#             cnt=cnt+1
# print(cnt)

