'''num = int(input())
reverse = 0
if num>0:
    while(num!=0):
      remainder = num%10
      reverse = reverse*10+remainder
      num = num//10
      print(reverse)
else:
    num=-1*num
    while(num>0):
        remainder = num%10
        reverse = reverse*10+remainder
        num = num//10
        print(-1*reverse)
'''
num = int(input())
givenInput = num
reverse = 0
if num < 0 :
    num =abs(num)
    while(num>0):
      remainder = num % 10
      reverse = reverse * 10 + remainder
      num = num // 10
    print(0-reverse)
elif num > 0:
    while(num>0):
        remainder = num % 10
        reverse = reverse * 10 + remainder
        num = num // 10
    print(reverse)
else:
    print(0)
