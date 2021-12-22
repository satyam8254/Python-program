def caseSort(s):
    s=list(s)
    lower=[]
    upper=[]
    for i in range(len(s)):
        if (s[i] >= 'a' and s[i] <= 'z'):
        #if s[i].islower():
            lower.append(s[i])
        elif (s[i] >= 'A' and s[i] <= 'Z'):
        #else:
            upper.append(s[i])
    lower=sorted(lower)
    upper=sorted(upper)
    Lindex=0
    Uindex=0
    for i in range(len(s)):
        if (s[i] >= 'a' and s[i] <= 'z'):
        #if s[i].islower():
            s[i]=lower[Lindex]
            Lindex=Lindex+1
        elif (s[i] >= 'A' and s[i] <= 'Z'):
        #else:
            s[i]=upper[Uindex]
            Uindex=Uindex+1
    return "".join(s)   
n=int(input())
s=input()[:n]
print(caseSort(s))