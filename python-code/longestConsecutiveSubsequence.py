# def longest_Consecutive_Subsequence(arr,n):
#     res_arr=[]
#     for i in range(0,n-1):
#         if arr[i+1]==arr[i]+1:
#             res_arr.append(arr[i])
#             return res_arr
# n=int(input())
# arr=[int(x) for x in input().split()]
# print(longest_Consecutive_Subsequence(arr,n))