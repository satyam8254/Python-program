testCase = int(input())
for i in range(testCase):
    totalBerth,berthNumber=map(int,input().split())
    if((berthNumber<0) or berthNumber>totalBerth):
        print("Invalid")
    else:
        if((berthNumber%8==1) or (berthNumber%8==4)):
            print("L")
        elif((berthNumber%8==2) or (berthNumber%8==5)):
            print("M")
        elif((berthNumber%8==3) or berthNumber%8==6):
            print("U")
        elif(berthNumber%8==7):
            print("SL")
        else:
            print("SU")


