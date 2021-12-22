def alphabet_occurance(string,alpha):
    count=0
    for i in string:
        if i==alpha:
            count=count+1
    return count
    if count>3:
        return True
    else:
        return False
#s='abdacdedgd'
#alphabet='d'
alphabet_occurance('abdacdedgd','d')
#print(result)