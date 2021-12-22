# def IsAnagram(s1,s2):
#     n1=len(s1)
#     n2=len(s2)
#     if n1!=n2:
#         return 0
#     c1=[0]*256
#     c2=[0]*256
#     for i in s1:
#         c1[ord(i)]+=1
#     for i in s2:
#         c2[ord(i)]+=1
#     for i in range(256):
#         if c1[i]!=c2[i]:
#             return 0
#     return 1

# s1=input()
# s2=input()
# print(IsAnagram(s1,s2))

# s1=input()
# s2=input()
# flag=0
# if len(s1)!=len(s2):
#     flag
# else:
#     for i in range(0,len(s1),1):
#         if i in range(0,len(s2),1):
#             flag=1
# if flag==1:
#     print(1)
# else:
#     print(0)

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
