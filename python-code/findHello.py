n=int(input())
s1=[]
for i in range(n):
    s=input()
    s1.append(s)
for i in range(len(s1)):
    #if len(s1[i])>0:
    if "hello" in s1[i]:
        print("Yes")
    else:
        print("No")
