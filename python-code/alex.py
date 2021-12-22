# string=input()
# print(string.swapcase())
string=input()
newString=""
for str in range(len(string)):
    if string[str].islower():
        newString=newString+string[str].upper()
    elif string[str].isupper():
        newString=newString+string[str].lower()
    else:
        newString=newString+string[str]
print(newString)