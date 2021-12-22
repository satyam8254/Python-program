def FirstUnique(string):
    d={}
    for i in string:
        if i not in d:
            d[i]=1
        else:
            d[i]=d[i]+1
    for i in range(len(string)):
        if d[string[i]]==1:
            return i
    return -1
n=int(input())
for i in range(n):
    string=input()
    print(FirstUnique(string))
