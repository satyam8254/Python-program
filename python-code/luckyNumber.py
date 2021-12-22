def findLuckyNumber(nums):
    # implement this function
    num={}
    for i in nums:
        if i in num:
            num[i]=num[i]+1
        else:
            num[i]=1
   
    for i in nums:  
        if num[i]==i:
            return i
    return -1


# DO NOT change anything below this line
if __name__ == "__main__":
    num_elems = int(input())
    input_arr = []
    for index in range(num_elems):
        input_arr.append(int(input()))
    
    print(findLuckyNumber(input_arr))