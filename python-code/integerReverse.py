def integerReverse(num):
    rev = 0
    while(num > 0):
        rem = num % 10
        rev = rev * 10 + rem
        num = num // 10
    return rev

n=int(input())
for i in range(n):
    num=int(input())
    print(integerReverse(num))