n=int(input())
arr=[int(x) for x in input().split()[:n]]
arr.sort(reverse=True)
M=""
N=""
for i in range(len(arr)):
    if i%2==0:
        M=M+str(arr[i])
    else:
        N=N+str(arr[i])
print(int(M)+int(N))
