n = int(input())
value = []
count = 0
for i in range(n):
    num = int(input())
    value.append(num)
    if value[0] == value[i]:
        count = count + 1
print(count)
