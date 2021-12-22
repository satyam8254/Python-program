letter=list(input().split()[:26])
s=input()
maxLetter=ord(max(s))
length=len(s)
maxLetterValue=letter[maxLetter-97]
area=(length)*1*(maxLetterValue)
# print(length)
# print(maxLetterValue)
print(area)