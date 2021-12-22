def intersect(nums1, nums2, nums3):
    # implement this function
    res=[]
    for i in range(len(nums1)):
        if nums1[i] in nums2 and nums1[i] in nums3:
            res.append(nums1[i])
    
    if res==[]:
        return[-1]
    else:
        return res
  
if __name__ == "__main__":
    num1_len = int(input())
    nums1 = []
    for index in range(num1_len):
        nums1.append(int(input()))
    num2_len = int(input())
    nums2 = []
    for index in range(num2_len):
        nums2.append(int(input()))
    num3_len = int(input())
    nums3 = []
    for index in range(num3_len):
        nums3.append(int(input()))

    for element in intersect(nums1, nums2, nums3):
        print(element)