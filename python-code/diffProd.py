def minDiff(arr, arr_size):
    l1=[]
    for i in range(arr_size):
        if arr[i]<arr[i+1]:
            l1.append(arr[i])


def maxDiff(arr, arr_size):
	

def prodDiff(arr, arr_size):
	### Complete this and the above functions!

for _ in range(int(input())):
    length = int(input())
    arr = [int(x) for x in input().split()]
    print(prodDiff(arr, length))