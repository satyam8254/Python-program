n = int(input())
nums =[]
ind = []
target = []
for i in range(n):
	nums.append(int(input()))
for i in range(n):
	ind.append(int(input()))
for i in range(len(nums)):
	temp = nums[i]
	target.insert(ind[i],temp)
for i in target:
    print(i)