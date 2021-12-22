def jhool(s):
    d={'r':0,'u':0,'b':0,'y':0}
    for i in s:
        if i in d:
            d[i]+=1
    return (d[min(d,key=d.get)])

tc=int(input())
for i in range(tc):
    s=input()
    print(jhool(s))