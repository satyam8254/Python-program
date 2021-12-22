s1=input()
s2=input()
string1=[]
string2=[]
for i in range(len(s1)):
    string1.append(s1[i])
for i in range(len(s2)):
    string2.append(s2[i])
if len(string1)==len(string2):
    for i in string1:
        if i in string2:
            string2.remove(i)
if len(string2)==0:
    print(1)
else:
    print(0)