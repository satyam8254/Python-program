def calSumUtil( A , B , n , m ): 
    # Implement this 
    # A is the first array
    # n is size of array A
    # B is the second array
    # m is size of array B
    A=A[::-1]
    B=B[::-1]
    res=[]
    carry=0
    for i in range(m):
        s=A[i]+B[i]+carry
        res.append(s%10)
        carry=s//10
    for i in range(m,n):
        s=A[i]+carry
        res.append(s%10)
        carry=s//10
    if carry!=0:
        res.append(carry)
    while len(res)>0 and res[-1]==0:
        res.pop()
    return res[::-1]


  
# Wrapper Function 
def calSum(a, b, n, m ): 
  
    # Making first array which have 
    # greater number of element
    # A is the first array
    # n is size of array A
    # B is the second array
    # m is size of array B 
    if n >= m: 
        return calSumUtil(a, b, n, m) 
    else: 
        return calSumUtil(b, a, m, n) 
  
# Driven Code 
testCase = int(input())
for _ in range(testCase):
	A = list(map(int,input().split()))
	B = list(map(int,input().split()))
	res = calSum(A, B, len(A), len(B))
	print(*res)