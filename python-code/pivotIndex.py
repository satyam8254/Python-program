def pivotIndex(arr):
    # Implement this function
    lSum=0
    rSum=sum(arr)-arr[0]
    if lSum==rSum:
        return 0
    for i in range(1,len(arr)):
        lSum=lSum+arr[i-1]
        rSum=rSum-arr[i]
        if lSum==rSum:
            return i
    return -1


# Do not edit anything below
if __name__ == "__main__":
    num_elems = int(input())
    nums = []
    for i in range(num_elems):
        nums.append(int(input()))
        
    print(pivotIndex(nums))