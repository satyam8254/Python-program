firstNumber = int(input())
secondNumber = int(input())
thirdNumber = int(input())
ratio = secondNumber /firstNumber
nterm =4
nextNumber = firstNumber * (ratio)**(nterm - 1)
print(int(nextNumber))