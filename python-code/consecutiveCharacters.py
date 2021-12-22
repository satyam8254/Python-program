string = input()
count = 0
count1 = []
s = string[0]
for i in range(len(string)):
    if s == string[i]:
        count = count+1
    else:
        count1.append(count)
        count = 1
        s = string[i]
    if i == len(string)-1:
        count1.append(count)
maxNum = count1[0]
for i in range(len(count1)):
    if count1[i] > maxNum:
        maxNum = count1[i]
print(maxNum)



















'''s=input()
count=1
arr=[]
if(len(s)==0):
    print(0)
else:
    for i in range(len(s)-1):
        if s[i]==s[i+1]:
            count=count+1
            arr.append(count)
print(max(arr))'''