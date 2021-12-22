testcase=int(input())
for i in range(testcase):
	n=int(input())
	ans = -1
	list1=list(map(int,input().split()))
	if(n == 1):
		ans = 1
		print(ans)
		continue
	if( list1[0]> list1[1]):
		ans = 1
		print(ans)
		continue
	for x in range(1,n-1):
		if( list1[x]> list1[x+1] and list1[x]>list1[x-1]):
		    ans = x+1
		    break
	if(list1[n-1] > list1[n-2] and ans == -1):
		ans = n
	print(ans)