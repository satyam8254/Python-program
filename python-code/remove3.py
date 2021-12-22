# your code goes here
import array
def intToArr(N):
    #complete this function
    a=array.array("d",[])
    a.append(N)
    return a

def remove_3(arr):
    #complete this function
    for i in range(len(arr)):
        if arr[i]==3:
            continue
        else:
            return (arr)

def arrToInt(arr):
    #complete this function
    res=remove_3(arr)
    return (res)

#DO NOT change anything below this line

N=int(input())
arrNum=intToArr(N)
arrNumWithout3=remove_3(arrNum)

print(arrToInt(arrNumWithout3))