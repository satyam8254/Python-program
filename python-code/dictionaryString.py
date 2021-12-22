def dictionaryString(s1,s2):
    for ch in s2:
        i=0
        for j in range(len(s1)):
            if ch[i]==s1[j]:
                i=i+1
            if i==len(ch):
                return len(ch)
    return 0
s1=input()
s2=input().split()
s2.sort(key=lambda x:len(x),reverse=True)
print(dictionaryString(s1,s2))