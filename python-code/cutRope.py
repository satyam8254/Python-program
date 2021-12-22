def cutRope(A):
    # Complete this function
    A.sort()
    res=[]
    count=0
    cuttingLength=A[0]
    for i in range(1,len(A)):
        if A[i]>cuttingLength:
            res.append(len(A)-i)
        cuttingLength=A[i]
        count+=1
    return res
# Do not change anything below this line
if __name__ == '__main__':
    input_numbers = []
    for _ in range(int(input())):
        input_numbers.append(int(input()))
    for i in cutRope(input_numbers):
        print(i)