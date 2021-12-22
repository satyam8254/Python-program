def halfInsertion(str):
    arr1=[]
    for i in str:
        arr1.append(i)
    for i in range((len(arr1)//2)+1,len(arr1)):
        j=i
        while (j>len(arr1)//2) and arr1[j]<arr1[j-1]:
            arr1[j],arr1[j-1]=arr1[j-1],arr1[j]
            j=j-1
    s="".join(arr1)
    return s
if __name__=='__main__':
    input_string = input()
    print(halfInsertion(input_string))