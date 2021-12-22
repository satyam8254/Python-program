# Inversion count


def inversionCount(arr, left, right):
    count = 0

    if right > left:
        mid = (left + right) // 2

        count += inversionCount(arr, left, mid) # [1, 6, 2, 4, 7] => [1, 2, 4, 6, 7] L[2]

        count += inversionCount(arr, mid + 1, right) # [3, 5, 10, 8, 9] => [3, 5, 8, 9, 10] R[0]

        count += merge(arr, left, mid, right)

    return count


def merge(arr, left, mid, right):
    tmp = [0] * (right - left + 1)

    i = left
    j = mid + 1
    k = 0

    invCount = 0

    while i <= mid and j <= right:
        if arr[i] < arr[j]:
            tmp[k] = arr[i]
            i += 1
        else: # L[i] > R[j]
            tmp[k] = arr[j]
            invCount += (mid - i + 1)
            j += 1

        k += 1

    while i <= mid:
        tmp[k] = arr[i]
        i += 1
        k += 1

    while j <= right:
        tmp[k] = arr[j]
        j += 1
        k += 1

    p = left

    for x in tmp:
        arr[p] = x
        p += 1

    return invCount


































# def inversionCount(arr, left, right):
#     count = 0

#     if right > left:
#         mid = (left + right) // 2

#         count += inversionCount(arr, left, mid)

#         count += inversionCount(arr, mid + 1, right)

#         count += merge(arr, left, mid, right)

#     return count

# def merge(arr, left, mid, right):
#     sorted = [0] * (right - left + 1)

#     inv_count = 0

#     i = left
#     j = mid + 1
#     k = 0

#     while i <= mid and j <= right:
#         if arr[i] <= arr[j]:
#             sorted[k] = arr[i]
#             i += 1
#         else: # arr[i] > arr[j] and i < j
#             sorted[k] = arr[j]
#             inv_count += (mid - i + 1)
#             j += 1

#         k += 1

#     while i <= mid:
#         sorted[k] = arr[i]
#         i += 1
#         k += 1

#     while j <= right:
#         sorted[k] = arr[j]
#         j += 1
#         k += 1

#     return inv_count

arr = [8, 4, 2, 1]

print(inversionCount(arr, 0, len(arr) - 1))

# (8, 4) (8, 2) (8, 1) (4, 2) (4, 1) (2, 1)
