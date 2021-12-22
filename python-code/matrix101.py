n,m=map(int,input().split())
matrix = []
sum1=0
for i in range(n):     
        matrix.append(list(map(int,input().split())))
for i in range(n):
	for j in range(m):
		if(matrix[i][j]%2==1):
			sum1=sum1+matrix[i][j]
print(sum1)


#time complexity = O(n*n)
#space complexity = O(n)



# n,m=map(int,input().split())
# matrix = [[]]*n
# sumOfOdd=0
# for i in range(n):
#     matrix[i]=list(map(int,input().split()))
#     if matrix[i]%2==1:
#         sumOfOdd=sumOfOdd+matrix[i]
# print(sumOfOdd)