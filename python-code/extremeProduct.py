n = int(input())
intvalue = []
for i in range(n):
    value = int(input())
    intvalue.append(value)
maxNum=max(intvalue)
minNum=min(intvalue)
extremeProduct = maxNum * minNum
print(extremeProduct)
