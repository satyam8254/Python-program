def stringInsertionSort(str):
    # Your code goes here
    arr=[]
    for i in str:
        arr.append(i)
    for i in range(1,len(arr)):
        j=i
        while j>0 and arr[j]<arr[j-1]:
            arr[j],arr[j-1]=arr[j-1],arr[j]
            j=j-1
    s="".join(arr)
    return s

### DO NOT CHANGE ANYTHING BELOW THIS LINE

if __name__=='__main__':
    input_string = input()
    print(stringInsertionSort(input_string))