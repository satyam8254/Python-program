n = int(input())
tribonacci=[0,0,1]
for i in range(3,n):
    num=tribonacci[i-1]+tribonacci[i-2]+tribonacci[i-3]
    tribonacci.append(num)
print(tribonacci[-1])
