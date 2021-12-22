num = int(input())
givenInput= num
sum = 0
while(num > 0):
    remainder = num%10
    num = num//10
    sum = sum +(remainder*remainder*remainder)

if sum!=givenInput or givenInput<=0:
  print("No")
else:
  print("Yes")   


