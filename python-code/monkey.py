for i in range(int(input())):
    str=input()
    dict={}
    for i in range(len(str)):
        if str[i] in dict:
            dict[str[i]]+=1
        else:
            dict[str[i]]=1
    matrix=[]
    for key,val in dict.items():
        matrix.append((key,val))
    matrix.sort(key=lambda x:ord(x[0]))
    matrix.sort(key=lambda x:x[1],reverse=True)
    print(matrix[0][0],matrix[0][1]) 
