def goal(command):
    res=""
    for i in range(len(command)):
        if command[i]!="(" and command[i]!=")":
            res=res+command[i]
        if command[i]=="(" and command[i+1]==")" and i+1<len(command):
            res=res+"o"
        if command[i]=="(":
            continue
        if command[i]==")":
            continue
    return res
command=input()
print(goal(command))