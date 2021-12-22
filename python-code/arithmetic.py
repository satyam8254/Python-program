print("enter first number")
firstNumber=int(input())
print("enter second number")
secondNumber=int(input())
print("enter third number")
thirdNumber=int(input())
difference=secondNumber - firstNumber
print("enter the nth term")
nterm = int(input()) 
#nterm=4
nextNumber= firstNumber + (nterm-1)*difference
print(nextNumber)