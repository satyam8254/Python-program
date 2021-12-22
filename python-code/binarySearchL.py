def binarysearch(arr, l, r, elem) :
    possible = -1
    while(l<=r) :
        mid = l + (r-l) // 2
        if arr[mid] == elem :
            possible = mid
            r = mid - 1
        elif arr[mid] > elem :
            r = mid  - 1
        else :
            l = mid + 1
    return possible
arr = [1,3,3,3]
elem = 3