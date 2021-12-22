import array
def shuffle(arr):
    # Implement this function
    arr1=[]
    arr2=[]
    arr3=[]
    for i in range(len(arr)//2):
        arr1.append(arr[i])
    for i in range(len(arr)//2,len(arr)):
        arr2.append(arr[i])
    for j in range(len(arr)//2):
        arr3.append(arr1[j])
        arr3.append(arr2[j])
    return arr3


# Do not edit anything below
if __name__ == "__main__":
    n = int(input())
    nums = []
    for index in range(2 * n):
        nums.append(int(input()))
    for elem in shuffle(nums):
        print(elem)

# def shuffle(arr):
#     # Implement this function
#     arr1=array.array("i",[])
#     arr2=array.array("i",[])
#     arr3=array.array("i",[])
#     for i in range(len(arr)//2):
#         arr1.append(arr[i])
#     for i in range(len(arr)//2,len(arr)):
#         arr2.append(arr[i])      
#     for j in range(len(arr)):
#         arr3.append(arr1[j])
#         arr3.append(arr2[j])
#     return arr3






















# import array
# arr1=array.array("i",[])
# arr2=array.array("i",[])
# size=int(input())
# for i in range(size):
#     num1=int(input())
#     num2=int(input())
#     arr1.append(num1)
#     arr2.append(num2)
