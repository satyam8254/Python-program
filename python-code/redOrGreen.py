color = input()
RedColor=0
greenColor=0
for i in range(0,len(color)):
    if color[i]=="R":
        RedColor=RedColor+1
    else:
        greenColor=greenColor+1

print(min(RedColor,greenColor))