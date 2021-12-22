def balanceParanthesis(start,openBracket,closeBracket,exp):
    if openBracket==0 and closeBracket==0:
        exp.append(start)
    if openBracket>0:
        balanceParanthesis(start+'(',openBracket-1,closeBracket,exp)
    if closeBracket>openBracket:
        balanceParanthesis(start+')',openBracket,closeBracket-1,exp)

def getAllBalancedParan(n):
    # Implement this function
    exp=[]
    start=""
    balanceParanthesis(start,n,n,exp)
    return exp


# Do not edit anything below
n = int(input())
allBalancedParan = getAllBalancedParan(n)
allBalancedParan.sort()
for expr in allBalancedParan:
    print(expr)





    #     if(n==0):
    #     return []
    # if(n==1):
    #     return ['()']
    # l1=getAllBalancedParan(n-1)
    # l2=[]
    # for x in l1:
    #     for i in range((len(x)//2)+1):
    #         s=str(x[:i+1])+'()'+str(x[i+1:])
    #         if(s not in l2):
    #             l2.append(s)
    # return l2