n = int(input())
sum = 0
for i in range(n):
    num = int(input())
    if num<0:
        continue
    else:
        sum = sum+num
print(sum)
