from collections import Counter
def bothCountX(string1, string2, x):
    # Complete this function, and return the list of resultant characters in sorted order
    s1=Counter(string1.lower())
    s2=Counter(string2.lower())
    res=[]
    for i in s1:
        if s1[i]==s2[i]==x:
            res.append(i)
    return (sorted(res))
for _ in range(int(input())):
    string1, string2, x = input().split()
    x = int(x)
    print(*bothCountX(string1, string2, x))
