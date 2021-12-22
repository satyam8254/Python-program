num = int(input())
givenInput = num
palindrome = 0
if num < 0 :
    num = abs(num)
    while(num > 0):
        lastDigit = num % 10
        palindrome = (palindrome*10) + lastDigit
        num = num - lastDigit
        num = num // 10
    print("True")
elif num > 0 :
    while(num > 0) :
        lastDigit = num % 10
        palindrome = (palindrome*10) + lastDigit
        num = num - lastDigit
        num = num // 10
    print("True")
else:
    print("False")

'''num = int(input())
givenInput = num
palindrome = 0
while(num > 0) :
    lastDigit = num % 10
    num = num - lastDigit
    palindrome = (palindrome*10) + lastDigit
    num = num // 10
if givenInput == palindrome:
    print("True")
else:
    print("False")'''
