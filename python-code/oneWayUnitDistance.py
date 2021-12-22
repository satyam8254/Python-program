def isEditDistanceOne(string1, string2): 
    # Complete this function, and return True/False
    if abs(len(string1)-len(string2))>1:
        return False
    count=0
    i=0
    j=0
    while i<len(string1) and j<len(string2):
        if string1[i]!=string2[j]:
            if count==1:
                return False
            if len(string1)>len(string2):
                i=i+1
            elif len(string1)<len(string2):
                j=j+1
            else:
                i=i+1
                j=j+1
            count=count+1
        else:
            i=i+1
            j=j+1
    if i<len(string1) or j<len(string2):
        count=count+1
    if count==1:
        return True
    else:
        return False

for _ in range(int(input())):
    input_string1, input_string2 = input().split()
    print(isEditDistanceOne(input_string1, input_string2))