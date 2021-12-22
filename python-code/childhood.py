from collections import defaultdict
n=int(input())
A=[-1]*256
d=defaultdict(int)
for i in range(n):
    a,b=input().lower().split()
    ordA,ordB=ord(a),ord(b)
    A[ordB if d[ordB]==0 else d[ordB]]=ordA
    A[ordA if d[ordA]==0 else d[ordA]]=ordB
    d[ordB],d[ordA]=ordA if d[ordA]==0 else d[ordA],ordB if d[ordB]==0 else d[ordB]
command=list(input())
for i in range(len(command)):
    ordd=ord(command[i])
    if (ordd>=65 and ordd<=90):
        if A[ord(command[i].lower())]!=-1:
            command[i]=chr(A[ord(command[i].lower())])
        command[i]=command[i].upper()
    else:
        if A[ord(command[i].lower())]!=-1:
            command[i]=chr(A[ord(command[i].lower())])
print("".join(command))